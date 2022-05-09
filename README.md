# Famous Painting Stylizer or PyTorch Neural Style Transfer With Flask App

#### Video Demo: https://www.youtube.com/watch?v=7Ok4RpL0_RU

## Overview:
For my CS50x final project, I coded a Flask app for users to modify pictures using an image transformation neural network. The U-Net first downsamples input image through a few convolutional layers; then, it feeds through some residual layers; finally, the network upsamples back into the original size and applies the ReLu activation function. In addition, instance normalization is applied to significantly improve the generated images. The neural network was implemented in PyTorch and from this [repository](https://github.com/pytorch/examples/tree/master/fast_neural_style).

## Files:
#### app.py
This file contains all the Flask code. There is only one app route. When you first open the website, you are presented with the index page through the "GET" method. After you submit the form, the computer collects the style name and chooses the corresponding model. The computer downloads the input image since the model runs locally. Afterwards, the GPU takes the inputed image and runs it through the model. The user is sent to the output page through the "POST" method. You can go back by clicking on the "Go Back" button. Even though the button is programmed like a form, it doesn't need Flask code because it uses the HTML function history.back().

#### style.py, transformer_net.py, utils.py
These are all modifications of files found in the repository from above.

#### layout.html
This file creates a layout for the Flask app. It has code for the sidebar, the footer, my app title, the header, and the "Open Sidebar" and "Go Back" buttons. There is some JavaScript for opening and closing the sidebar. I got it from this [website](https://www.w3schools.com/howto/howto_js_collapse_sidebar.asp).

#### index.html
This is the homepage, or the page that first pops up on when you visit the link. It uses Jinja2 to use the layout template. There is code to let the user upload an image, but most of the code is to let the user choose a style. The "Stylize!" button submits the Flask form and redirects the user to the output page.

#### output.html
I got the idea of having an output page from the Week 9 Finance assignment. Furthermore, this page extends the layout template and displays a downloadable output image.

#### styles.css
This file contains the pallette for the site and my design choices. I wanted the user to see the painting the filter was based on, so I found some [code](https://stackoverflow.com/questions/17541614/use-images-instead-of-radio-buttons) from stack exchange that allows you to overlay radio buttons with images. When a user hovers over their selection, the image becomes clearer.

#### main.js
The code found in this file is a drop box that lets you upload your images. I got it from this [website](https://codepen.io/dcode-software/pen/xxwpLQo).

#### saved_models
This folder contains all the models that you can use to stylize your images, including the ones I downloaded from the repo and the five models I trained.

#### Serena.jpg, thumb.png
I think that these fun additions make my website more appealing.

#### requirements.txt
Run "pip install -r requirements.txt" to install required packages.

## Certain Design Choices and Explanation:
I wanted to add an extra page with information, but I an additional information page was unnecessary. Instead, I choose to create a simple and neat sidebar. I decided to use a model from the PyTorch repo library after digging through GitHub. Next, I implemented radio buttons so the user can only choose one style at a time. At first, I created a dropdown list with the names of the filters, but this method allows the user to see the original painting which will style their pictures. A bright purple color is used on the site because it catches the eye and it's my favorite color.

## Best Part of My Project:
The best part of my project was finally completing it. I'm glad that the deadline for CS50x is December 2021, because I definitely wouldn't have finished this in one week. It took me a long time to settle on a project, and then a model. I wanted my project to be fun and challenging. After finishing this app, I was really satisfied to see the result and reflect on my experiences to complete the assignment.

## Conclusion:
This course has helped me learn a lot about the various applications of coding, and this final project wrapped it up for me. Now, I know how logic and calculations work in coding and the inner workings of a computer. I'm proud that I made a whole Flask app that is organized nicely, compiles, and completes a task.