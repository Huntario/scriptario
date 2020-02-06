Scriptario
Apply network analysis to screenplays

A web application that scans screenplays in PDF format,
and creates network graphs of location, scene, and character.
The purpose of this software is to provide an open source method
for filmmakers to plan films in the most logistically effecient way possible.

Requirements
Scriptario:
1. Takes a PDF file as user input
2. Converts those PDFs to text data
--Assuming standard screenplay format--
3. Identifies list of locations
4. Identifies scenes within those locations
5. Identifies chracters within those scenes
6. Counts words of each character
7. Lists data based on location, scene, or chracter
8. Present data to user
----------------------------------------------------
▲▼ React Frontend
1. UI based API
- https://www.freecodecamp.org/news/create-a-react-frontend-a-node-express-backend-and-connect-them-together-c5798926047c/
- https://programmingwithmosh.com/javascript/react-file-upload-proper-server-side-nodejs-easy/
----------------------------------------------------
▲▼ Node middleware 
- serves React frontend and serves as interface between it and services
- https://www.npmjs.com/package/pdf-to-text
----------------------------------------------------
◀ ▶ Python graphing app
(Takes a text script) --> returns a network graph
1. pdfminer.six
-  https://pdfminersix.readthedocs.io/en/latest/api/index.html
-  https://github.com/pdfminer/pdfminer.six
-----

100 Questions
1. How is this better than other solutions?
2. Can I factor in my budget in any way? 
3. Can it give me estimated times at each location based on a config value?
4. Can it give me scene by scene PDFs?
5. Can it give me actor specific script packets?
6. Can it include schedule/location information with that packet?
