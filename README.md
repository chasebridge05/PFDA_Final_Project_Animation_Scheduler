# PFDA_Final_Project_Animation_Scheduler

## Demo
Demo Video: https://youtu.be/KpyHKJfcd5Y

## GitHub Repository
GitHub Repo: https://github.com/chasebridge05/PFDA_Final_Project_Animation_Scheduler.git

## Description
So my project went through a few changes since the conception of the idea, and in the end became more of a helping tool for scheduling within the animation pipeline. In short, what my project will do is allow a project manager to enter in an employee's name, availability in hour per week, and what role that they play in the animation pipeline. In addition to workers, they are able to add in different projects that are being worked on with their planned start and ending dates and from that it will create a comma separated values (or csv) file.
Whereas originally this csv file would use scheduling logic to create a schedule, it now is a consolidation of information that will put every date within a timeframe, every project and every worker into a csv spreadsheet that will allow a project manager to be able to see any person's avaliabilty for any given day. Since I wasn't able to get the scheduling logic to work, I wanted to at least make sure that csv for formatted well and was readable for different purposes.
The formatting of the code is simple in explaining as my main function sets the output for inputs within the terminal, the functions to add workers and projects do just that, and the function to generate the schedule consolidates the information and sets the format of the csv file.
I used the pandas third party library which was really helpful for getting the information inputted to be output as if it were a spreadsheet. I also used the datetime library from Python which was helpful in making sure that every date within a start and ending time frame was accounted for and that all dates were formatted correctly.
As for future areas of improvment, I think the obvious one is to try and figure out scheduling logic within the context of this code to turn it into less of a scheduling tool and more of a scheduler. I also think, and I did try to get this to work but I just couldn't quite get it, is to allow project managers to be able to input days that workers are unavilable that will be factored into the spreadsheet. As for now though, the csv file can be edited and you can remove people on specific days if needed.
In the end, I am very proud of what I was able to make with the knowledge that I've learned, but I won't lie and say that I am not upset that I couldn't create the project I first thought of.