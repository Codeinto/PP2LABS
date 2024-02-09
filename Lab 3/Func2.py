movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

N1
def scorecheck(m):
    s=input("movie: ")
    for i in m:
        if i["name"]==s and i["imdb"]>5.5:
            return True
            break
print(score(movies))

N2
def above(m):
    for i in m:
        if i["imdb"]>5.5:
            print(i["name"])
above(movies)

N3
def category(m):
    s=input("category: ")
    for i in m:
        if i["category"]==s:
            print(i["name"])
category(movies)

N4
def average(m):
    s,c=0,0
    for i in m:
        c+=1
        s+=i["imdb"]
    return s/c
print(average(movies))

N5
def cataverage(m):
    s,c=0,0
    x=input("category: ")
    for i in m:
        if i["category"]==x:
            c+=1
            s+=i["imdb"]
    return s/c
print(cataverage(movies))