 For Running Application :  uvicorn app.main:app --reload

 here is launch.json for debugger visual studio 
 {
   // Use IntelliSense to learn about possible attributes.
   // Hover to view descriptions of existing attributes.
   // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
   "version": "0.2.0",
   "configurations": [
     {
       "name": "Python: Uvicorn",
       "type": "python",
       "request": "launch",
       "module": "uvicorn",
       "args": ["app.main:app", "--reload"],
       "cwd": "${workspaceFolder}",
       "env": {
         "DEBUG": "1"
       }
     }
   ]
 }
