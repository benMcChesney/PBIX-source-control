# README

#### Version 0.0.1 


## Introduction
This python package is used to extract a .pbix file and store it for use in a readable format insource control. Then rezip the files into a usable format. This gives the benefit of compatibility but a deeper level of source control and changes. 


## Dependencies

- no external libraries
- Python 3+

## IDE

added files for VS Code in /.vscode

### Command Arguments

To get detailed cmd line help run the following command:
```bash
python pbix_utils.py --help
```


```bash
python pbix_utils.py "<PATH TO PBIX>.pbix" --extract 1 --combine 1  --extract_file_endings "<path_to_SCHEMA>.json"
```


- path       
  - relative path to a .pbix file, to be extracted