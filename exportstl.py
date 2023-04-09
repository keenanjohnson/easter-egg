'''
exportstl
===

Demos 307 redirects with the Onshape API
'''

from apikey.client import Client

# stacks to choose from
stacks = {
    'cad': 'https://cad.onshape.com'
}

# create instance of the onshape client; change key to test on another stack
c = Client(stack=stacks['cad'], logging=True)

document_id = "e881b494a6dd7064d2a177b7"
workspace_id = "f1110229c856013a0ade4c6e"
element_id = "fc812dd1da7540830b9082aa"

# get the STL export
stl = c.part_studio_stl(document_id, workspace_id, element_id)

# print to the console
#print(stl.text)

with open("part.stl", "w") as text_file:
    text_file.write(stl.text)
