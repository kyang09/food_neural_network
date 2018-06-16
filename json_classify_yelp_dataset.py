import json
import csv

good_reviews = []
bad_reviews = []

good_reviews_eval = []
bad_reviews_eval = []

food_categories = set()
food_business_ids = set()

with open("data/dataset/review.json.1.aa.ac") as r1, open("data/dataset/review.json.1.ab.ad") as r2:
    with open("data/dataset/business.json") as b:
        with open('yelp_food_categories.txt') as food_categories_csv:
            cat_list = list(food_categories_csv)
            for cat in cat_list:
                bothCatFormats = cat.split(", ")
                food_categories.add(bothCatFormats[0])
                food_categories.add(bothCatFormats[1])
            
            business_list = list(b)
            for bus in business_list:
                b_data = json.loads(bus)
                for c in b_data["categories"]:
                    if (c in food_categories):
                        food_business_ids.add(b_data["business_id"])

            reviews = r1.readlines()
            reviews_eval = r2.readlines()

            reviews_stripped = [x.strip() for x in reviews]
            reviews_eval_stripped = [x.strip() for x in reviews_eval]
            
            for rev in reviews_stripped:
                data = json.loads(rev)

                if (data["business_id"] in food_business_ids):
                    if (data["stars"] > 3.0):
                        good_reviews.append(data["text"].replace("\n", ""))
                    else:
                        bad_reviews.append(data["text"].replace("\n", ""))

            for rev_eval in reviews_eval_stripped:
                data = json.loads(rev_eval)

                if (data["business_id"] in food_business_ids):
                    if (data["stars"] > 3.0):
                        good_reviews_eval.append(data["text"].replace("\n", ""))
                    else:
                        bad_reviews_eval.append(data["text"].replace("\n", ""))

with open("data/dataset/good_reviews.txt", "w") as gr:
    for good_rev in good_reviews:
        gr.write("%s . \n" % good_rev)

with open("data/dataset/bad_reviews.txt", "w") as br:
    for bad_rev in bad_reviews:
        br.write("%s . \n" % bad_rev)

with open("data/dataset/good_reviews_eval.txt", "w") as gr:
    for good_rev_eval in good_reviews_eval:
        gr.write("%s . \n" % good_rev_eval)

with open("data/dataset/bad_reviews_eval.txt", "w") as br:
    for bad_rev_eval in bad_reviews_eval:
        br.write("%s . \n" % bad_rev_eval)
