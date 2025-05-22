# Working with local LLMs using LM-Studio
This repository contains examples on how to work with local LLMs using LM-Studio both with text-prompts as well as image input.

## Chat Example
The chat example works by using plain html with a bit of javascript.
1. Download a small model in LM-Studio
2. Go into the LM-Studio Settings and check *Enable Local LLM Service*
3. Go to the developer tab and activate *Enable CORS* and *Server on Local Network*
4. In the developer tab, load a model and start the server
5. Open the html file in your browser 

## Image Input
Working with images is a bit more complicated, because we need to set up a separate server using Node.js.
1. Download a vision-enabled model in LM-Studio
2. Specify the model in the *server.js* file (the correct line is marked with a comment)
3. Install Node.js and make sure everything is working properly
4. In the terminal, navigate into the *image-description-app* folder
5. Run *npm install* to install all necessary dependencies
6. Run *node server.js* to start the server on *http://localhost:3000*
7. Open *http://localhost:3000* in a browser