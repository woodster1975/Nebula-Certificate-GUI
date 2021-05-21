import sys
import os
import time
import pathlib
import subprocess
from jinja2 import *


try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk


try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True


def set_Tk_var():
    global name
    name = tk.StringVar()


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


def create_cert(string, name):
    created = False
    filename = name + ".crt"
    try:
        exists = check_exist(filename)
        if not exists:
            os.system(string)
            time.sleep(1)
            exists = check_exist(filename)
            if exists:
                created = True

            else:
                created = False
    except:
        created = False
    return created


def check_exist(filename):
    path = pathlib.Path(filename)
    exists = path.exists()
    return exists


def get_cert_details(name):
    cmd = "nebula-cert.exe print -path " + name + ".crt"
    out = subprocess.check_output(cmd, shell=False)
    return out


def set_Tk_var():
    global che44
    che44 = tk.IntVar()


def check_exist(filename):
    time.sleep(1)
    path = pathlib.Path(filename)
    exists = path.exists()
    return exists


template = "config.j2"


def config(ca_filename, crt_filename, key_filename, name):
    ca, crt, key = read_files(ca_filename, crt_filename, key_filename)
    with open(template) as f:
        config_template = f.read()
        templated_config = Template(config_template)
        output = templated_config.render(ca=ca, crt=crt, key=key)
        write_yml(output, name)


def write_yml(output, name):
    f = open(f"{name}-config.yml", "a")
    f.write(output)
    f.close()


def read_files(ca_filename, crt_filename, key_filename):
    f = open(ca_filename, "r")
    ca = f.read()
    f.close()

    f = open(crt_filename, "r")
    crt = f.read()
    f.close()

    f = open(key_filename, "r")
    key = f.read()
    f.close()
    return ca, crt, key


if __name__ == "__main__":
    import main
    main.vp_start_gui()
