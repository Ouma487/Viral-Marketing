INSTAGRAM_POSTS
id_user: identifiant de l'utilisateur (6 chiffres)
id_post: identifiant du post (9 chiffres)
date: date du post
time: heure du post
half_day: am ou pm
views: nombre de vues du post
reposts: nombre de personnes qui ont partagé le post
likes: nombre de likes du post
comments: nombre de commentaires sur le post
id_post_origin: identifiant du post à partir duquel on a partagé l'information (si id_post_origin = 0 : le post a été créé sans partage)
link_clicks: booléen ; True  si des utilisateurs originaires de ce post sont allés sur le site Greenpeace
donation_tag: booléen ; True  si des utilisateurs originaires de ce post ont ensuite effectué une donation sur le site Greenpeace
donation_val: si donation_tag = True, valeur des donations en question
house_buy: booléen ; True si des utilisateurs originaires de ce post ont acheté une maison

INSTAGRAM_ACCOUNTS
id_user: identifiant de l'utilisateur (6 chiffres)
nb_followers: nombre de personnes qui follow cet utilisateur (parmi les 3000 users du dataset)
nb_following: nombre de personnes que l'utilisateur follow (parmi les 3000 users du dataset)
nb_posts: nombre de posts de l'utilisateur
sex: male ou female
id_followers: liste des identifiants des personnes qui follow cet utilisateur (parmi les 3000 users du dataset)
department: département d'habitation principale de l'utilisateur
email: email de l'utilisateur
user_agent: agent utilisateur principal identifié pour l'utilisateur
birth_date: date de naissance de l'utilisateur