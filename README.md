# apriltag-gen

Generate all ids for 36h11 tags with different sizes as follows:

| Tag ID Range | Tag Size (mm) | Example tag                    |
| ------------ | ------------- | ------------------------------ |
| [0,150]      | 150           | [tag id 100](output/tag36_11_00100.pdf) |
| [151,300]    | 100           | [tag id 200](output/tag36_11_00200.pdf) |
| [301,450]    | 50            | [tag id 400](output/tag36_11_00400.pdf) |
| [451,586]    | 20            | [tag id 500](output/tag36_11_00500.pdf) |

Generated tags in [the output folder](output/).

# Setup

- Clone this repo (with --recurse-submodules to make sure you get the contents of the repositories added as submodules)
- Install Python 3 and pip3. 
- Install virtualenv:
```$ pip3 install virtualenv```
- Edit **Makefile** to reflect the right paths to python 3 and pip3 on your system.

# Run

```$ make run```

The script will generate the ouptut pdfs in folder ```output/```

