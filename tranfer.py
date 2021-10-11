
import os


def replaceName(name):
    name = name.replace("IJCAI2020", "")
    name = name.replace("IJCAI2021", "")
    name = name.replace("ICML2020", "")
    name = name.replace("ICML2021", "")
    name = name.replace("ICDE2020", "")
    name = name.replace("ICDE2021", "")
    name = name.replace("WWW_2020_", "")
    name = name.replace("WWW_2021_", "")
    return name

if __name__ == "__main__":
    
    for parent, dirnames, filenames in os.walk(os.getcwd()):
        if parent.count(".git") != 0 or filenames == [] or parent.count("\\") <= 3:
            continue
        # print(parent, dirnames)
        task = parent.split("\\")
        for filename in filenames:
            filename = replaceName(filename)
            # print(filename)
            with open("result.csv", "a+", 100000) as f:
                filename = filename.replace("\xad", " ")
                filename = filename.replace("\u2217", "")
                print(filename)
                f.write(task[len(task) - 2] + "\t" + task[len(task) - 1] + "\t" + filename + "\n")
        # for filename in filenames:
        #     file_path = os.path.join(parent, filename)
        #     print(file_path)