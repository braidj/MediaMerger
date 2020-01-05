
# -------------------------------------------------------------------------------------------
# Created: 20200105 Jason Braid
# Following tutorial on https://stackabuse.com/reading-and-writing-yaml-to-a-file-in-python/
# -------------------------------------------------------------------------------------------

import yaml

if __name__ == "__main__":
    # -----------------------------------------------------------------------------
    # Purpose: main code block called
    # -----------------------------------------------------------------------------

    print("Following config is being used")
    config_file = r"D:\Dropbox\Jason\Development\Python\yaml\media_merger_cfg.yml"

    with open(r'fruits.yaml') as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        fruits_list = yaml.load(file, Loader=yaml.FullLoader)

        print(fruits_list)

    with open(r'categories.yaml') as file:
        documents = yaml.full_load(file)

        for item, doc in documents.items():
            print(item, ":", doc)
