import pandas as pd
from PIL import Image
from bokeh.plotting import figure, output_file, show
import math
from bokeh.palettes import Purples
from bokeh.transform import cumsum
from bokeh.models import LabelSet, ColumnDataSource
import streamlit as st
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer
import time
time.clock = time.time
bot=ChatBot('Counselor')
trainer = ListTrainer(bot)
trainer1 = ChatterBotCorpusTrainer(bot)
p=1
trainer1.train("chatterbot.corpus.english.greetings")
trainer.train(["Hi,who are you","I am a career counseling bot","What can you do?","I can choose a good career for you",'How to take my test',"Enter 'start my test'"])

def get_text():
    x=st.text_input("YOU : ")
    response = bot.get_response(x)
    y="start my test"
    if( y in x.lower()):
        global p
        p=0
        response='Here you go...'
    return response

qvals = {"None": 0, "Strongly Agree": 5, "Agree": 4, "Neutral": 3, "Disagree": 2,"Strongly Disagree": 1}
st.title("CAREER COUNSEL BOT")
banner=Image.open("img\ss1.png")
st.image(banner, use_column_width=True)    
st.header("ABOUT US : ")
st.write("Hi!!\nI am your career counsellor bot and I will be helping you to clear the block that you have on persuing the field of your interest\n\nIf you type 'start my test' - a short QUIZ will be held to understand you and thereby I give results of the top 5 professions for you\n")
answerz = get_text()
st.text_area("COUNSELLOR BOT : ", value=answerz, height=100, max_chars=None)
     
if(p==0):
    st.title("PERSONALITY TEST : ")
    st.write("GOOD LUCK !! ")
    s = st.selectbox("WHAT IS YOUR HIGHEST QUALIFICATION?",["None","10th","12th","UG"])
    lis = []

    if (s == "10th"):
                st.title("SUBJECTS THAT CAN BE PERSUED")
                img0=Image.open("img\ss0.png")
                st.image(img0, use_column_width=True)
                st.write("1.  Computers\n2.  Mathematics\n3.  Chemistry\n4.  Biology\n5.  Physics\n6.  Commerce\n7.  Psychology\n8.  History\n9.  Physical Education\n10.  Design\n\n")
                
                st.header("\nQUESTION 1:")
                st.write("I like to write a lot of computer programs\n")
                img11=Image.open("img\ss13.png")
                st.image(img11, use_column_width=True)
                q1=st.selectbox("ENTER AN OPTION......",["None","Strongly Agree","Agree","Neutral","Disagree","Strongly Disagree"],key = '1')
                
                if ((q1 != "None")):
                    lis.append(qvals[q1])
                    st.header("\nQUESTION 2:")
                    st.write("I can easily understand and solve mathematical problems\n")
                    img12=Image.open("img\ss14.png")
                    st.image(img12, use_column_width=True)
                    q2=st.selectbox("ENTER AN OPTION......",["None","Strongly Agree","Agree","Neutral","Disagree","Strongly Disagree"],key = '2')

                    if (q2 != "None"):
                        lis.append(qvals[q2])
                        st.header("\nQUESTION 3:")
                        st.write("I would love to learn more about chemical components and reactions\n")
                        img13=Image.open("img\ss15.png")
                        st.image(img13, use_column_width=True)
                        q3=st.selectbox("ENTER AN OPTION......",["None","Strongly Agree","Agree","Neutral","Disagree","Strongly Disagree"],key = '3')

                        if (q3 != "None"):
                            lis.append(qvals[q3])
                            st.header("\nQUESTION 4:")
                            st.write("Learning more on survival of plants and animals is my passion\n")
                            img14=Image.open("img\ss16.png")
                            st.image(img14, use_column_width=True)
                            q4=st.selectbox("ENTER AN OPTION......",["None","Strongly Agree","Agree","Neutral","Disagree","Strongly Disagree"],key = '4')

                            if (q4 != "None"):
                                lis.append(qvals[q4])
                                st.header("\nQUESTION 5:")
                                st.write("I find the interaction between the fundamental constituents of the universe to be Fascinating\n")
                                img15=Image.open("img\ss17.png")
                                st.image(img15, use_column_width=True)
                                q5=st.selectbox("ENTER AN OPTION......",["None","Strongly Agree","Agree","Neutral","Disagree","Strongly Disagree"],key = '5')

                                if (q5 != "None"):
                                    lis.append(qvals[q5])
                                    st.header("\nQUESTION 6:")
                                    st.write("I enjoy myself while working on Accounting and Business Management\n")
                                    img16=Image.open("img\ss18.png")
                                    st.image(img16, use_column_width=True)
                                    q6=st.selectbox("ENTER AN OPTION......",["None","Strongly Agree","Agree","Neutral","Disagree","Strongly Disagree"],key = '6')

                                    if (q6 != "None"):
                                        lis.append(qvals[q6])
                                        st.header("\nQUESTION 7:")
                                        st.write("I would like to expand my knowledge on human behaviour, relation sand patterns of thinking\n")
                                        img17=Image.open("img\ss19.png")
                                        st.image(img17, use_column_width=True)
                                        q7=st.selectbox("ENTER AN OPTION......",["None","Strongly Agree","Agree","Neutral","Disagree","Strongly Disagree"],key = '7')

                                        if (q7 != "None"):
                                            lis.append(qvals[q7])
                                            st.header("\nQUESTION 8:")
                                            st.write("I like to venture about the events from the past\n")
                                            img18=Image.open("img\ss20.png")
                                            st.image(img18, use_column_width=True)
                                            q8=st.selectbox("ENTER AN OPTION......",["None","Strongly Agree","Agree","Neutral","Disagree","Strongly Disagree"],key = '8')

                                            if (q8 != "None"):
                                                lis.append(qvals[q8]) 
                                                st.header("\nQUESTION 9:")
                                                st.write("I am a person who is more inclined towards sports and fitness\n")
                                                img19=Image.open("img\ss21.png")
                                                st.image(img19, use_column_width=True)
                                                q9=st.selectbox("ENTER AN OPTION......",["None","Strongly Agree","Agree","Neutral","Disagree","Strongly Disagree"],key = '9')

                                                if (q9 != "None"):
                                                    lis.append(qvals[q9])
                                                    st.header("\nQUESTION 10:")
                                                    st.write("I enjoy creating works of arts")
                                                    img20=Image.open("img\ss22.png")
                                                    st.image(img20, use_column_width=True)
                                                    q10=st.selectbox("ENTER AN OPTION......",["None","Strongly Agree","Agree","Neutral","Disagree","Strongly Disagree"],key = '10')

                                                    if (q10 != "None"):
                                                        lis.append(qvals[q10])
                                                        st.success("TEST COMPLETED")
                                                        print(lis)
                                                        st.title("RESULTS")
                                                        data = pd.read_csv(r'Occupations.csv', encoding= 'windows-1252')

                                                        input_list = lis

                                                        subjects = {1: "Computers",
                                                                2: "Mathematics",
                                                                3: "Chemistry",
                                                                4: "Biology",
                                                                5: "Physics",
                                                                6: "Commerce",
                                                                7: "Psychology",
                                                                8: "History",
                                                                9: "Physical Education",
                                                                10: "Design"}

                                                        def output(listofanswers):
                                                            class my_dictionary(dict):
                                                                def _init_(self):
                                                                    self = dict()
                                                                def add(self, key, value):
                                                                    self[key] = value
                                                            
                                                            ques = my_dictionary()

                                                            for i in range(0, 10):
                                                                ques.add(i, input_list[i])

                                                            all_scores = []

                                                            for i in range(9):
                                                                all_scores.append(ques[i] / 5)

                                                            li = []

                                                            for i in range(len(all_scores)):
                                                                li.append([all_scores[i], i])
                                                            li.sort(reverse=True)
                                                            sort_index = []
                                                            for x in li:
                                                                sort_index.append(x[1] + 1)
                                                            all_scores.sort(reverse=True)
                                                            
                                                            a = sort_index[0:5]
                                                            b = all_scores[0:5]
                                                            s = sum(b)
                                                            d = list(map(lambda x: x * (100 / s), b))

                                                            return a, d

                                                        l, data = output(input_list)

                                                        out = []
                                                        for i in range(0, 5):
                                                            n = l[i]
                                                            c = subjects[n]
                                                            out.append(c)

                                                        output_file("pie.html")

                                                        graph = figure(title="Recommended professions", height=500,
                                                                       width=500)
                                                        radians = [math.radians((percent / 100) * 360) for percent
                                                                       in data]

                                                        start_angle = [math.radians(0)]
                                                        prev = start_angle[0]
                                                        for i in radians[:-1]:
                                                            start_angle.append(i + prev)
                                                            prev = i + prev

                                                        end_angle = start_angle[1:] + [math.radians(0)]

                                                        x = 0
                                                        y = 0

                                                        radius = 1.0

                                                        color = Purples[len(out)]
                                                        graph.xgrid.visible = False
                                                        graph.ygrid.visible = False
                                                        graph.xaxis.visible = False
                                                        graph.yaxis.visible = False

                                                        for i in range(len(out)):
                                                            graph.wedge(x, y, radius,
                                                                        start_angle=start_angle[i],
                                                                        end_angle=end_angle[i],
                                                                        color=color[i],
                                                                        legend_label=out[i] + "-" + str(
                                                                            round(data[i])) + "%")
                                                                            
                                                        graph.add_layout(graph.legend[0], 'right')
                                                        show(graph, use_container_width=True)
                                                        labels = LabelSet(x='text_pos_x', y='text_pos_y',
                                                                            text='percentage', level='glyph',
                                                                            angle=0, render_mode='canvas')
                                                        graph.add_layout(labels)
    elif (s == "12th"):
                st.title("STREAMS THAT CAN BE PERSUED")
                img02=Image.open("img\ss02.png")
                st.image(img02, use_column_width=True)
                st.write("1.  Law\n2.  Healthcare\n3.  Management\n4.  Engineering\n5.  Finance\n6.  Sports\n7.  Language and Communication\n8.  Performing Arts\n9.  Applied and Visual Arts\n10.  Science and Mthematics\n11.  Clerical and Secretarial\n12.  Social Status\n13.  Education and Social Support\n14. Military/Armed Force\n14.  Marketing and Sales\n\n")

                st.header("\nQUESTION 1:")
                st.write("I love to debate and negotiate issues in public\n")
                img21=Image.open("img\ss23.png")
                st.image(img21, use_column_width=True)
                q1=st.selectbox("ENTER AN OPTION......",["None","Strongly Agree","Agree","Neutral","Disagree","Strongly Disagree"],key = '1')
                
                if ((q1 != "None")):
                    lis.append(qvals[q1])
                    st.header("\nQUESTION 2:")
                    st.write("I like to study the Anatomy of the human body and help people who are in need of first aid\n")
                    img22=Image.open("img\ss24.png")
                    st.image(img22, use_column_width=True)
                    q2=st.selectbox("ENTER AN OPTION......",["None","Strongly Agree","Agree","Neutral","Disagree","Strongly Disagree"],key = '2')

                    if (q2 != "None"):
                        lis.append(qvals[q2])
                        st.header("\nQUESTION 3:")
                        st.write("I have team spirit and leadership qualities\n")
                        img23=Image.open("img\ss25.png")
                        st.image(img23, use_column_width=True)
                        q3=st.selectbox("ENTER AN OPTION......",["None","Strongly Agree","Agree","Neutral","Disagree","Strongly Disagree"],key = '3')

                        if (q3 != "None"):
                            lis.append(qvals[q3])
                            st.header("\nQUESTION 4:")
                            st.write("I find working with tools, equipment, and machinery to be enjoyable\n")
                            img24=Image.open("img\ss26.png")
                            st.image(img24, use_column_width=True)
                            q4=st.selectbox("ENTER AN OPTION......",["None","Strongly Agree","Agree","Neutral","Disagree","Strongly Disagree"],key = '4')

                            if (q4 != "None"):
                                lis.append(qvals[q4])
                                st.header("\nQUESTION 5:")
                                st.write("Budgeting, costing and estimating for a business is fascinating\n")
                                img25=Image.open("img\ss27.png")
                                st.image(img25, use_column_width=True)
                                q5=st.selectbox("ENTER AN OPTION......",["None","Strongly Agree","Agree","Neutral","Disagree","Strongly Disagree"],key = '5')

                                if (q5 != "None"):
                                    lis.append(qvals[q5])
                                    st.header("\nQUESTION 6:")
                                    st.write("I like to take part in competitive sporting events as a professional\n")
                                    img26=Image.open("img\ss28.png")
                                    st.image(img26, use_column_width=True)
                                    q6=st.selectbox("ENTER AN OPTION......",["None","Strongly Agree","Agree","Neutral","Disagree","Strongly Disagree"],key = '6')

                                    if (q6 != "None"):
                                        lis.append(qvals[q6])
                                        st.header("\nQUESTION 7:")
                                        st.write("I enjoy doing translations, reading and correcting language\n")
                                        img27=Image.open("img\ss29.png")
                                        st.image(img27, use_column_width=True)
                                        q7=st.selectbox("ENTER AN OPTION......",["None","Strongly Agree","Agree","Neutral","Disagree","Strongly Disagree"],key = '7')

                                        if (q7 != "None"):
                                            lis.append(qvals[q7])
                                            st.header("\nQUESTION 8:")
                                            st.write("I want to act or direct a play or a film\n")
                                            img28=Image.open("img\ss30.png")
                                            st.image(img28, use_column_width=True)
                                            q8=st.selectbox("ENTER AN OPTION......",["None","Strongly Agree","Agree","Neutral","Disagree","Strongly Disagree"],key = '8')

                                            if (q8 != "None"):
                                                lis.append(qvals[q8]) 
                                                st.header("\nQUESTION 9:")
                                                st.write("I see making sketches of people(portraits) as my career\n")
                                                img29=Image.open("img\ss31.png")
                                                st.image(img29, use_column_width=True)
                                                q9=st.selectbox("ENTER AN OPTION......",["None","Strongly Agree","Agree","Neutral","Disagree","Strongly Disagree"],key = '9')

                                                if (q9 != "None"):
                                                    lis.append(qvals[q9])
                                                    st.header("\nQUESTION 10:")
                                                    st.write("I love to work with a lot of numbers and calculations\n")
                                                    img30=Image.open("img\ss32.png")
                                                    st.image(img30, use_column_width=True)
                                                    q10=st.selectbox("ENTER AN OPTION......",["None","Strongly Agree","Agree","Neutral","Disagree","Strongly Disagree"],key = '10')

                                                    if (q10 != "None"):
                                                        lis.append(qvals[q10])
                                                        st.header("QUESTION 11")
                                                        st.write("I like to do the clerical works like issueing reciepts, filing and counting stack\n")
                                                        img31=Image.open("img\ss33.png")
                                                        st.image(img31, use_column_width=True)
                                                        q11 = st.selectbox("ENTER AN OPTION......",["None","Strongly Agree","Agree","Neutral","Disagree","Strongly Disagree"], key='11')
                                                        
                                                        if (q11 != "None"):
                                                            lis.append(qvals[q11])
                                                            st.header("Question 12")
                                                            st.write("I love to study the life style of human societies\n")
                                                            img32=Image.open("img\ss34.png")
                                                            st.image(img32, use_column_width=True)
                                                            q12 = st.selectbox("ENTER AN OPTION......",["None","Strongly Agree","Agree","Neutral","Disagree","Strongly Disagree"], key='12')
                                                            
                                                            if (q12 != "None"):
                                                                lis.append(qvals[q12])
                                                                st.header("Question 13")
                                                                st.write("I want to teach children and young people on a daily basis\n")
                                                                img33=Image.open("img\ss35.png")
                                                                st.image(img33, use_column_width=True)
                                                                q13 = st.selectbox("ENTER AN OPTION......",["None","Strongly Agree","Agree","Neutral","Disagree","Strongly Disagree"], key='13')
                                                                
                                                                if (q13 != "None"):
                                                                    lis.append(qvals[q13])
                                                                    st.header("Question 14")
                                                                    st.write("I won't have a problem persevering in the army or police force\n")
                                                                    img34=Image.open("img\ss36.png")
                                                                    st.image(img34, use_column_width=True)
                                                                    q14 = st.selectbox("ENTER AN OPTION......",["None","Strongly Agree","Agree","Neutral","Disagree","Strongly Disagree"],key='14')
                                                                    
                                                                    if (q14 != "None"):
                                                                        lis.append(qvals[q14])
                                                                        st.header("Question 15")
                                                                        st.write("I like to introduce new products and sell them in the minds of the people - I may beable to influence people a bit")
                                                                        img35=Image.open("img\ss37.png")
                                                                        st.image(img35, use_column_width=True)
                                                                        q15 = st.selectbox("ENTER AN OPTION......",["None","Strongly Agree","Agree","Neutral","Disagree","Strongly Disagree"],key='15')
                                                                        
                                                                        if (q15 != "None"):
                                                                            lis.append(qvals[q10])
                                                                            st.success("Test Completed")
                                                                            #st.write(lis)
                                                                            st.title("RESULTS:")
                                                                            df = pd.read_csv(r"Graduate.csv")

                                                                            input_list = lis

                                                                            streams = {1: "Law",
                                                                                       2: "Healthcare",
                                                                                       3: "Management",
                                                                                       4: "Engineering",
                                                                                       5: "Finance",
                                                                                       6: "Sports",
                                                                                       7: "Language and communication",
                                                                                       8: "Performing Arts",
                                                                                       9: "Applied and Visual arts",
                                                                                       10: "Science and math",
                                                                                       11: "Clerical and secretarial",
                                                                                       12: "Social Science",
                                                                                       13: "Education and Social Support",
                                                                                       14: "Armed Forces",
                                                                                       15: "Marketing and sales"}
                                                                            
                                                                            def output(listofanswers):
                                                                                class my_dictionary(dict):
                                                                                    def _init_(self):
                                                                                        self = dict()
                                                                                    def add(self, key, value):
                                                                                        self[key] = value
                                                                                
                                                                                ques = my_dictionary()

                                                                                for i in range(0, 10):
                                                                                    ques.add(i, input_list[i])

                                                                                all_scores = []

                                                                                for i in range(9):
                                                                                    all_scores.append(ques[i] / 5)

                                                                                li = []

                                                                                for i in range(len(all_scores)):
                                                                                    li.append([all_scores[i], i])
                                                                                li.sort(reverse=True)
                                                                                sort_index = []
                                                                                for x in li:
                                                                                    sort_index.append(x[1] + 1)
                                                                                all_scores.sort(reverse=True)
                                                                                
                                                                                a = sort_index[0:5]
                                                                                b = all_scores[0:5]
                                                                                s = sum(b)
                                                                                d = list(map(lambda x: x * (100 / s), b))

                                                                                return a, d

                                                                            l, data = output(input_list)

                                                                            out = []
                                                                            for i in range(0, 5):
                                                                                n = l[i]
                                                                                c = streams[n]
                                                                                out.append(c)

                                                                            output_file("pie.html")

                                                                            graph = figure(title="Recommended professions", height=500,
                                                                                        width=500)
                                                                            radians = [math.radians((percent / 100) * 360) for percent
                                                                                        in data]

                                                                            start_angle = [math.radians(0)]
                                                                            prev = start_angle[0]
                                                                            for i in radians[:-1]:
                                                                                start_angle.append(i + prev)
                                                                                prev = i + prev

                                                                            end_angle = start_angle[1:] + [math.radians(0)]

                                                                            x = 0
                                                                            y = 0

                                                                            radius = 0.8

                                                                            color = Purples[len(out)]
                                                                            graph.xgrid.visible = False
                                                                            graph.ygrid.visible = False
                                                                            graph.xaxis.visible = False
                                                                            graph.yaxis.visible = False

                                                                            for i in range(len(out)):
                                                                                graph.wedge(x, y, radius,
                                                                                            start_angle=start_angle[i],
                                                                                            end_angle=end_angle[i],
                                                                                            color=color[i],
                                                                                            legend_label=out[i] + "-" + str(
                                                                                                round(data[i])) + "%")

                                                                            graph.add_layout(graph.legend[0], 'right')
                                                                            show(graph, use_container_width=True)
                                                                            labels = LabelSet(x='text_pos_x', y='text_pos_y',
                                                                                                text='percentage', level='glyph',
                                                                                                angle=0, render_mode='canvas')
                                                                            graph.add_layout(labels)
    elif (s == "UG"):
                st.title("AVAILABLE FIELDS")
                img=Image.open("img\ss2.png")
                st.image(img, use_column_width=True)
                st.write("1.  Systems Security Administrator\n2.  Business Systems Analyst\n3.  Software Systems Engineer\n4.  Database Devolper\n5.  Business Intelligent Analyst\n6.  CRM Technical Developer\n7.  Mobile Application Developer\n8.  UX Designer\n9.  Quality Assurance Associate\n10.  Web Developer\n\n")
                
                st.header("\nQUESTION 1:")
                st.write("Company can hire me to handle all the aspects of INFORMATION SECURITY and protect its VIRTUAL DATA RESOURCES\n")
                img1=Image.open("img\ss3.png")
                st.image(img1, use_column_width=True)
                q1=st.selectbox("ENTER AN OPTION......",["None","Strongly Agree","Agree","Neutral","Disagree","Strongly Disagree"],key = '1')
                
                if ((q1 != "None")):
                    lis.append(qvals[q1])
                    st.header("\nQUESTION 2:")
                    st.write("Studying an organization's business and information requirements and developing processes to meet its strategic goals is something I enjoy\n")
                    img2=Image.open("img\ss4.png")
                    st.image(img2, use_column_width=True)
                    q2=st.selectbox("ENTER AN OPTION......",["None","Strongly Agree","Agree","Neutral","Disagree","Strongly Disagree"],key = '2')

                    if (q2 != "None"):
                        lis.append(qvals[q2])
                        st.header("\nQUESTION 3:")
                        st.write("I can assess a quandary and design a pristinely incipient system or amend a subsisting system to make it better and more efficient\n")
                        img3=Image.open("img\ss5.png")
                        st.image(img3, use_column_width=True)
                        q3=st.selectbox("ENTER AN OPTION......",["None","Strongly Agree","Agree","Neutral","Disagree","Strongly Disagree"],key = '3')

                        if (q3 != "None"):
                            lis.append(qvals[q3])
                            st.header("\nQUESTION 4:")
                            st.write("Designing, developing, modifying, editing and working with databases and immensely colossal datasets is my cup of tea\n")
                            img4=Image.open("img\ss6.png")
                            st.image(img4, use_column_width=True)
                            q4=st.selectbox("ENTER AN OPTION......",["None","Strongly Agree","Agree","Neutral","Disagree","Strongly Disagree"],key = '4')

                            if (q4 != "None"):
                                lis.append(qvals[q4])
                                st.header("\nQUESTION 5:")
                                st.write("I can mine data utilizing BI software implements, compare, visualize and communicate the results with facileness\n")
                                img5=Image.open("img\ss7.png")
                                st.image(img5, use_column_width=True)
                                q5=st.selectbox("ENTER AN OPTION......",["None","Strongly Agree","Agree","Neutral","Disagree","Strongly Disagree"],key = '5')

                                if (q5 != "None"):
                                    lis.append(qvals[q5])
                                    st.header("\nQUESTION 6:")
                                    st.write("Implementing and providing support for Microsoft's Dynamics CRM is a adeptness I possess\n")
                                    img6=Image.open("img\ss8.png")
                                    st.image(img6, use_column_width=True)
                                    q6=st.selectbox("ENTER AN OPTION......",["None","Strongly Agree","Agree","Neutral","Disagree","Strongly Disagree"],key = '6')

                                    if (q6 != "None"):
                                        lis.append(qvals[q6])
                                        st.header("\nQUESTION 7:")
                                        st.write("I can be innovative and ingenious when it comes to making utilizer-cordial mobile applications\n")
                                        img7=Image.open("img\ss9.png")
                                        st.image(img7, use_column_width=True)
                                        q7=st.selectbox("ENTER AN OPTION......",["None","Strongly Agree","Agree","Neutral","Disagree","Strongly Disagree"],key = '7')

                                        if (q7 != "None"):
                                            lis.append(qvals[q7])
                                            st.header("\nQUESTION 8:")
                                            st.write("I can perform well in a varied discipline, coalescing aspects of psychology, business, market research, design, and technology\n")
                                            img8=Image.open("img\ss10.png")
                                            st.image(img8, use_column_width=True)
                                            q8=st.selectbox("ENTER AN OPTION......",["None","Strongly Agree","Agree","Neutral","Disagree","Strongly Disagree"],key = '8')

                                            if (q8 != "None"):
                                                lis.append(qvals[q8]) 
                                                st.header("\nQUESTION 9:")
                                                st.write("I am responsible enough to maintain the quality systems, such as laboratory control and document control and training, to ascertain control of the manufacturing process\n")
                                                img9=Image.open("img\ss11.png")
                                                st.image(img9, use_column_width=True)
                                                q9=st.selectbox("ENTER AN OPTION......",["None","Strongly Agree","Agree","Neutral","Disagree","Strongly Disagree"],key = '9')

                                                if (q9 != "None"):
                                                    lis.append(qvals[q9])
                                                    st.header("\nQUESTION 10:")
                                                    st.write("Be it front-end or back-end, I would dote designing and developing websites more than anything else")
                                                    img10=Image.open("img\ss12.png")
                                                    st.image(img10, use_column_width=True)
                                                    q10=st.selectbox("ENTER AN OPTION......",["None","Strongly Agree","Agree","Neutral","Disagree","Strongly Disagree"],key = '10')

                                                    if (q10 != "None"):
                                                        lis.append(qvals[q10])
                                                        st.success("TEST COMPLETED")
                                                        print(lis)
                                                        st.title("RESULTS")
                                                        data = pd.read_csv(r'Occupations.csv', encoding= 'windows-1252')

                                                        input_list = lis

                                                        professions = {1: "Systems Security Administrator",
                                                                    2: "Business Systems Analyst",
                                                                    3: "Software Systems Engineer",
                                                                    4: "Database Developer",
                                                                    5: "Business Intelligence Analyst",
                                                                    6: "CRM Technical Developer",
                                                                    7: "Mobile Applications Developer",
                                                                    8: "UX Designer",
                                                                    9: "Quality Assurance Associate",
                                                                    10: "Web Developer"}
                                                        def output(listofanswers):
                                                            class my_dictionary(dict):
                                                                def _init_(self):
                                                                    self = dict()
                                                                def add(self, key, value):
                                                                    self[key] = value
                                                            
                                                            ques = my_dictionary()

                                                            for i in range(0, 10):
                                                                ques.add(i, input_list[i])

                                                            all_scores = []

                                                            for i in range(9):
                                                                all_scores.append(ques[i] / 5)

                                                            li = []

                                                            for i in range(len(all_scores)):
                                                                li.append([all_scores[i], i])
                                                            li.sort(reverse=True)
                                                            sort_index = []
                                                            for x in li:
                                                                sort_index.append(x[1] + 1)
                                                            all_scores.sort(reverse=True)
                                                            
                                                            a = sort_index[0:5]
                                                            b = all_scores[0:5]
                                                            s = sum(b)
                                                            d = list(map(lambda x: x * (100 / s), b))

                                                            return a, d

                                                        l, data = output(input_list)

                                                        out = []
                                                        for i in range(0, 5):
                                                            n = l[i]
                                                            c = professions[n]
                                                            out.append(c)

                                                        output_file("pie.html")

                                                        graph = figure(title="Recommended professions", height=500,
                                                                       width=500)
                                                        radians = [math.radians((percent / 100) * 360) for percent
                                                                       in data]

                                                        start_angle = [math.radians(0)]
                                                        prev = start_angle[0]
                                                        for i in radians[:-1]:
                                                            start_angle.append(i + prev)
                                                            prev = i + prev

                                                        end_angle = start_angle[1:] + [math.radians(0)]

                                                        x = 0
                                                        y = 0

                                                        radius = 0.8

                                                        color = Purples[len(out)]
                                                        graph.xgrid.visible = False
                                                        graph.ygrid.visible = False
                                                        graph.xaxis.visible = False
                                                        graph.yaxis.visible = False

                                                        for i in range(len(out)):
                                                            graph.wedge(x, y, radius,
                                                                        start_angle=start_angle[i],
                                                                        end_angle=end_angle[i],
                                                                        color=color[i],
                                                                        legend_label=out[i] + "-" + str(
                                                                            round(data[i])) + "%")

                                                        graph.add_layout(graph.legend[0], 'right')
                                                        show(graph, use_container_width=True)
                                                        labels = LabelSet(x='text_pos_x', y='text_pos_y',
                                                                            text='percentage', level='glyph',
                                                                            angle=0, render_mode='canvas')
                                                        graph.add_layout(labels)
                                                       
                                                        