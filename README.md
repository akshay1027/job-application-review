## contact info:
- phoneNumber: +91 8056701263
- emailId : akshayar1027@gmail.com
- linkedin : https://www.linkedin.com/in/akshayrr1027/


## Job application review system:

- create application ✅
- update application | email, name, skills ✅
- upload and update resume ✅
- delete application ✅
- get one particular application ✅
- get all applications ✅
- ability to make an application selected or rejected ✅
- get all selected applications ✅
- get all rejected applications ✅
- filter all applications by name and or email ✅
- filter all applications based on skill ✅

- TODO (minimum):
1) It should have api endpoints to create, retrieve, update, delete and list the information of an applicant. ✅
2) It should also have a feature to mark applicants Selected or rejected. ✅

- TODO (extra):
1) Upload Resume and store as URL ✅
2) API Documentation (but in postman) ✅
3) Filtering Applications ✅

- TODO (my own):
1) Extra filters ✅
2) Extra update APIs ✅
3) Multiple jobs (it is a job (single job) review system but still mutiple jobs feature can be added in future) ❌


## Postman documentation of API

- NOTE: toogle each request, the grey colour ones are the request and response tested in local env and saved.
[link](https://www.postman.com/akshayrr27/workspace/akshay-r-r/collection/11715636-f749778d-435b-452c-b3ed-f248569371d9?action=share&creator=11715636)
![image](https://user-images.githubusercontent.com/65683151/190662166-366de626-da3c-4701-8cff-a3e040c9011e.png)


## Engineering decisions taken during class hours 😅:

![IMG_20220916_115557](https://user-images.githubusercontent.com/65683151/190665482-4d2364ac-7f3f-460f-9030-a276984b886f.jpg)
![IMG_20220916_115544](https://user-images.githubusercontent.com/65683151/190665493-6a3303e8-c3cd-49ba-b476-1f6631e67234.jpg)


## Architecture/design decisons:

- I have kept the Application model small as of now as its a project to test my coding ability. Eg: Emitted fields like Phone_number, Degree etc deliberately, for the reasons stated before.

- UUID is better for performing queries faster.

- For patch request, dont keep ending slash
  https://stackoverflow.com/questions/2712682/how-to-select-a-record-and-update-it-with-a-single-queryset-in-django

- Eg: Backend developer and frontend developer jobs exist.
      So if a user applied for backend role, they can't apply for frontend with same email id due to current design having email id as unique field.

  Sol: Use uuid or shorter ID instead, i used email before to get an application uniquely as its easier by now how to go with id only.

- Eg: UUID vs Normal ID : https://stackoverflow.com/a/58737923/13946919
 
- How to upload file:
1) Install pillow.
2) Make necessary changes in settings file for configuration of files.
3) Define the model.
4) Define the serializer.
5) Define the view.
EG: Resume uploaded: http://127.0.0.1:8000/static/resumes/3a5fa5e4-21c9-21ce-b0eb-d5d335275f2d.pdf

- [Q for filtering](https://books.agiliq.com/projects/django-orm-cookbook/en/latest/query_relatedtool.html)

- Mumble api
- django documentation
- stackoverflow

job-mail