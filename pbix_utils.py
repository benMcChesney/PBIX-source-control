import zipfile
import os
import argparse
import json

file_path = 'CHANGE ME'


def zipdir(root_path, ziph):
    
    # ziph is zipfile handle
    for root, dirs, files in os.walk(root_path):
        for file in files:
            #print('file', file )
            path =  os.path.join(root, file)

            new_path = path 
            if path.find( root_path) >= 0 :
                #print('path has root in it ! ', ) 
                new_path = path[ len( root_path ):]
                #print('new_path', new_path )

            ziph.write(path, new_path)
           

def add_file_endings(schema, directory):

    for f in schema['files']['json']:
        # get the original path ( without file ending ) and specify the output
        src_path = f"{directory}\\{f}"
        tar_path = src_path + '.json'
        
        if os.path.exists(src_path):
            print(f"'{ src_path}' -> '{tar_path}'")

            # remove renamed file if it already exists
            if os.path.isfile(tar_path):
                os.remove(tar_path)
                
            with open(src_path, 'r') as input:
                print(type(input))
                output = open(tar_path, 'w')
                data = input.read()
                output.write(data) 

def remove_file_endings(schema, directory):

    for f in schema['files']['json']:
        # get the original path ( without file ending ) and specify the output
        src_path = f"{directory}\\{f}"
        tar_path = src_path + '.json'
        # remove renamed file if it already exists
        if os.path.isfile(tar_path):
            os.remove(tar_path)

if __name__ == '__main__':

    # parse command args 
    parser = argparse.ArgumentParser()
    parser.add_argument("path"
                        ,help="relative path to a .pbix file, to be extracted"
                        ,type=str)

    parser.add_argument("--extract" 
                        ,help="take the given path input and extract it to a folder structure.")
   
    parser.add_argument("--combine" 
                        ,help="combine the directory of extracted files in path")
   
    parser.add_argument("--extract_file_endings" 
                        ,help="add file endings to extracted files, and remove them before being recombined.")
   
    args = parser.parse_args()

    file_path = args.path
    export_dir = f"./{file_path[0:-5]}_extracted"


    if args.extract:
        # unzipping the file
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(export_dir)
            print(f"zip {file_path} -> dir {export_dir}" )

    pbix_schema = ''
    if args.extract_file_endings:
        schema_path = args.extract_file_endings
        with open(schema_path) as json_file:
            pbix_schema = json.load(json_file)
            add_file_endings( pbix_schema, export_dir )

    if args.combine:
        rezipped_path = f"{file_path[0:-5]}_rezipped.pbix"

        if args.extract_file_endings:
            remove_file_endings( pbix_schema, export_dir )
        zipf = zipfile.ZipFile(rezipped_path, 'w', zipfile.ZIP_DEFLATED)
        zipdir(export_dir, zipf)
        zipf.close()
        print('dir combined into ->', rezipped_path )