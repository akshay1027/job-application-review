- For patch request, dont keep ending slash
- https://stackoverflow.com/questions/2712682/how-to-select-a-record-and-update-it-with-a-single-queryset-in-django


Job application review system:

- create application
- update application
- delete application
- get one particular application
- get all applications 
- ability to make an application selected or rejected 
- get all selected applications
- get all rejected applications
- Filter all applications that have a particular skillset, eg: python iruka application matum filter out


Architecture/design decisons:

- Eg: Backend developer and frontend developer jobs exist.
      So if a user applied for backend role, they can't apply for frontend with same email id due to current design having email id as unique field.
  Sol: Use uuid or shorter ID instead, i used email before to get an application uniquely as its easier by now how to go with id only.

- Eg: Add JobID field to model.

- Eg: UUID vs Normal ID : https://stackoverflow.com/a/58737923/13946919
 



- TODO (minimum):
1) Upload Resume and store as URL
2) Swagger Documentation
3) Filtering applications using keywords from skills

- TODO (extra):
1) Multiple jobs
