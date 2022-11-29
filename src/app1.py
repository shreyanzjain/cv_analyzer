import nltk
import numpy as np
import pandas as pd
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

import docx2txt

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def conform():
    txt1 = docx2txt.process('./uploads/cv1.docx')
    txt3 = docx2txt.process('./uploads/cv2.docx')
    txt4 = docx2txt.process('./uploads/cv3.docx')

    # print(result)

    txt2 = '''
    Introduction\
    At IBM, work is more than a job - it\'s a calling: To build. To design. To code. To consult. To think along with clients and sell. To make markets. To invent. To collaborate. Not just to do something better, but to attempt things you\'ve never thought possible. Are you ready to lead in this new era of technology and solve some of the world\'s most challenging problems? If so, lets talk.\
    Your Role and Responsibilities\
    You will solve the problems that may occur in IBM products, operating systems, networks, databases, applications, third party products as well as custom codes.\
    Become a Security SME for our flagship products family of Access Management product.\
    Analyze customer problems and service requests and resolve them within agreed service levels\
    Use troubleshooting/ debugging techniques and tools to analyze technical problems.\
    Collaborate with development teams for issues that need a resolution through code fixes.\
    Increase IBM\'s Self-Help knowledge base by creating knowledge articles wherever needed.\
    Provide feedback to the development team on product feature enhancements.\
    Create wikis, blogs, tech-notes, technical trainings, webcasts for educating customer and business partners\
    Technical: Must have\
    • Knowledge of SAML/ Federation, Openid, Docker, Web Services, RestAPI\
    • Troubleshooting network issues - SSL concepts and Network traces (wireshark, iptrace)\
    • Knowledge of Network security, TCP/IP fundamentals, http protocol\
    • Javascripts, XML, JSON\
    • Experience on any Access Manager product (IBM, Oracle, Siteminder, Ping, Sailpoint, Okta etc)\
    Required Technical and Professional Expertise\
    • Knowledge of LDAP/AD, Database, Access manager product\
    • Knowledge of Cloud and Container concept is a plus\
    • Basic Operating Systems skills for Unix / Linux.\
    • Knowledge of any Webserver and Application servers\
    • Virtualization concepts – Vmware/ESX etc\
    • Perl/Shell scripting, any programming language\
    Preferred Technical And Professional Expertise\
    • Proven communication skills\
    • Listening skills. Analytical and problem-solving skills\
    • Ability to work as a part of a global team, despite the diversity (cultural, geographic and other differences)\
    About Business Unit\
    IBM’s Cloud and Cognitive software business is committed to bringing the power of IBM’s Cloud and Watson/AI technologies to life for our clients and ecosystem partners around the world. IBM provides you with the most comprehensive and consistent approach to development, security and operations across hybrid environments—with complete software solutions for business and IT operations, development, data science, security, and management. Our experts and software capabilities help organizations develop applications once and deploy them anywhere, integrate security across the breadth of their IT estate, and automate operations with management visibility. With IBM, you also have access to new skills and methods, governance and management approaches, and a deep ecosystem of industry experts and partners.\
    This job requires you to be fully COVID-19 vaccinated prior to your start date and proof of vaccination status will be required before your start date. During the Onboarding process you will be asked to confirm your vaccination status, in case you are unable to get vaccinated for any reason, you can let us know at that stage. Please let us know if you are unable to be vaccinated due to medical or religious reasons. IBM will consider such requests on a case by case basis subject to submission of required proof by the candidate before a stipulated date.\
    Your Life @ IBM\
    Are you craving to learn more? Prepared to solve some of the world\'s most unique challenges? And ready to shape the future for millions of people? If so, then it\'s time to join us, express your individuality, unleash your curiosity and discover new possibilities.\
    Every IBMer, and potential ones like yourself, has a voice, carves their own path, and uses their expertise to help co-create and add to our story. Together, we have the power to make meaningful change – to alter the fabric of our clients, of society and IBM itself, to create a truly positive impact and make the world work better for everyone.\
    It\'s time to define your career.\
    About IBM\
    IBM’s greatest invention is the IBMer. We believe that through the application of intelligence, reason and science, we can improve business, society and the human condition, bringing the power of an open hybrid cloud and AI strategy to life for our clients and partners around the world.Restlessly reinventing since 1911, we are not only one of the largest corporate organizations in the world, we’re also one of the biggest technology and consulting employers, with many of the Fortune 50 companies relying on the IBM Cloud to run their business. At IBM, we pride ourselves on being an early adopter of artificial intelligence, quantum computing and blockchain. Now it’s time for you to join us on our journey to being a responsible technology innovator and a force for good in the world.\
    Location Statement\
    When applying to jobs of your interest, we recommend that you do so for those that match your experience and expertise. Our recruiters advise that you apply to not more than 3 roles in a year for the best candidate experience.\
    For additional information about location requirements, please discuss with the recruiter following submission of your application.\
    Being You @ IBM\
    IBM is committed to creating a diverse environment and is proud to be an equal opportunity employer. All qualified applicants will receive consideration for employment without regard to race, color, religion, gender, gender identity or expression, sexual orientation, national origin, genetics, pregnancy, disability, age, veteran status, or other characteristics. IBM is also committed to compliance with all fair employment practices regarding citizenship and immigration status
    '''
    cv = CountVectorizer()

    textList = [txt1, txt2]
    textList2 = [txt3, txt2]
    textList3 = [txt4, txt2]

    count_matrix = cv.fit_transform(textList)
    count_matrix1 = cv.fit_transform(textList2)
    count_matrix2 = cv.fit_transform(textList3)

    percentMatch = cosine_similarity(count_matrix)
    percentMatch1 = cosine_similarity(count_matrix1)
    percentMatch2 = cosine_similarity(count_matrix2)

    otpt1 = round(percentMatch[0][1] * 100,2)
    otpt2 = round(percentMatch1[0][1] * 100,2)
    otpt3 = round(percentMatch2[0][1] * 100,2)

    list01 = []

    list01.append(otpt1)
    list01.append(otpt2)
    list01.append(otpt3)

    list01.sort(reverse=True)

    # names = ['You', 'Someone', 'Someone']
    # indexes = ['1', '2', '3']

    # df = pd.DataFrame({'Rank': indexes, 'Percent Match': list01, 'Name': names})

    # df['Name'] = names
    # df['Rank'] = indexes

    return list01

# Export(df)