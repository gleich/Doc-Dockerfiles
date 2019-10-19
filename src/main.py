import os
import subprocess
import argparse

import request_utils


def main():
    """Runs the Auto-Doc-Dockerfiles program
    """
    # Argument parser:
    parser = argparse.ArgumentParser(description="Parser for the program")
    parser.add_argument("-u", "--dockerUsername", type=str,
                        help="Name of the user that has all the images on docker-hub")
    parser.add_argument("-p", "--folderPath", type=str,
                        help="The location from root of the folder or git repo where the folders of images are")
    args = parser.parse_args()
    folder_path = args.folderPath
    docker_username = args.dockerUsername
    # Loading template before moving directories
    with open("template.txt", "r") as template_file:
        README_template = template_file.read()
    # Changing directory into the location of the folders of images are
    os.chdir(folder_path)
    # Getting location of all the Dockerfiles
    path_of_all_dockerfiles = os.popen(
        'find . -name "Dockerfile"').read().split("\n")
    dockerfiles_to_check = []
    for path in path_of_all_dockerfiles:
        files_around_dockerfile = os.listdir(
            path_of_all_dockerfiles).strip("Dockerfile")
        if "README.md" in files_around_dockerfile:
            dockerfiles_to_check.append(path)
    # Meat of it all, get meta data on Docker Hub and create the README.md
    for path in dockerfiles_to_check:
        folder_name = path.strip("Dockerfile").split("/")[-1]
        image_meta_data = request_utils.get_image_meta(
            docker_username, folder_name)
        if image_meta_data != None:
            docker_hub_url = "https://hub.docker.com/r/" + \
                docker_username + "/" + folder_name
            registry_info = "[View on DockerHub](" + docker_hub_url + ")"
            description = image_meta_data["description"]
        else:
            registry_info = "**Not on Docker Hub**"
            description = "No description, look in Dockerfile"
        filled_template = README_template.format(dockerID=docker_username, imageName=folder_name,
                                                 description=description, registry=registry_info)
        intermediate_txt_file_path = path.strip(
            "Dockerfile") + "/README.txt"
        subprocess.call(["touch", intermediate_txt_file_path])
        with open(intermediate_txt_file_path, "w") as intermediate_txt_file:
            intermediate_txt_file.write(filled_template)
        subprocess.call(["mv", intermediate_txt_file_path, path.strip(
            "Dockerfile") + "/README.MD"])
        print("Created README.md in")
