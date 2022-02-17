Sample Assessment - sastaticket.pk
Project Objective
Create a Resume Collection Web Application
Success Criteria
Application contains A users and one superuser.
A User can Upload a cv, add relevant information* for
it. A User can associated two types of tags in it.
Tag one will related to a Users Skill(for example, the programming languages the user knows)
Tag two will be a general tags.
Think of these tags as hashtags in twitter.
A User can search based on
the information add
tags for different CV's. The user can also add references to the cv of another user.
*: This is upto your decision of what information is relevant but it should make sense for searching
capabilities and the overall use case.
Tasks
Your task is as follows:
1. Develop the authentication module using AbstractBaseUser of Django and Token Authentication.
2. Develop the related models for the use-case as you see fit. Please put comments on models to
explain your design decisions if any.
3. Develop one APIViewSet just for Resume resource(all curd operations). Nothing for users etc is
needed.
4. Develop one APIView for getting the full reference chain of any resume resource. i.e User1 was
referred by User2 who was referred by User3 and so on.
5. Dockerize the complete project.


Document objective Done:
1. Inherit AbstractBaseUser and add phone_number as req field
2. Configure JWT Authentication (we can use Token Auth here to0)
3. Configure signup, gettoken, refresh token endpoints
4. Configure Resume model with filefield and (oneTomany relationship) with user model
5. CRUD for Resumes and search filter with override SEARCH_PARAM as hashtag
6. Configure Reference model my (onetomany relationship)
7. In Serializer I tried but (short of time and lot of issues) so, I hve done it normally but we can use here recursion func for chain creation as well as (by 2 models "refer_to" and "refer_by" we can make nested serializer OR serializer relations may be)
8. Add postman collection for all endpoints
9. push to public repo


*Apologize for taken too much time with not 100% work*