from ruamel import yaml



if __name__ == "__main__":
    #-----------------------------------------------------------------------------
    # Purpose: main code block called
    #-----------------------------------------------------------------------------

    print("Following config is being used")
    config_file = r"D:\Dropbox\Jason\Development\Python\yaml\media_merger_cfg.yml"

    # TODO Add a list to the YAML file and see how it is stored.

    with open(config_file, 'r') as fp:
        config_dict = yaml.load(fp, Loader=yaml.Loader)
        print (config_dict)

        for key in config_dict:
            print("%s = %s" % (key, config_dict[key]))