import pandas as pd
import statistics
from pprint import pprint

conversion_map = {
  'USA': 'United States'
}

country_list = {}
data_frame = pd.read_csv("metal_bands.csv")
for index, row in data_frame.iterrows():
    print(row['origin'], row['fans'])
    if not row['origin'] in country_list:
        country_list[row['origin']] = {}
        country_list[row['origin']]['fans'] = []
        country_list[row['origin']]['formed'] = row['formed']
        country_list[row['origin']]['split'] = row['split']
    country_list[row['origin']]['fans'].append(row['fans'])

# pprint(country_list)
# for (country, fans) in country_list.items():
#     print("['{}', {}],".format(country, statistics.mean(fans)))

# curr_year = 1970
# year_structure = []
# while curr_year < 2017:
#     year_structure.append({
#       'year': curr_year,
#       'USA': [],
#       'United Kingdom': [],
#       'Germany': [],
#       'Sweden': [],
#       'Finland': [],
#     })
#     for index, row in data_frame.iterrows():
#         if row['origin'] not in list(year_structure[-1].keys()):
#             continue
#         print(row['formed'])
#         if (
#             row['formed'] == '-' or int(row['formed']) <= curr_year
#         ) and (
#             row['split'] == '-' or int(row['split']) >= curr_year
#         ):
#             print("{}: {}".format(row['formed'], curr_year))
#             year_structure[-1][row['origin']].append(row['fans'])
#     curr_year += 1

# for year_obj in year_structure:
#     for (country, popularity) in year_obj.items():
#         if country == 'year':
#             continue
#         if len(popularity) > 1:
#             year_obj[country] = statistics.mean(popularity)
#         elif len(popularity) == 0:
#             year_obj[country] = 0
#         else:
#             year_obj[country] = popularity[0]

# pprint(year_structure)
# import json
# with open('data.json', 'w', encoding='utf-8') as f:
#     json.dump(year_structure, f, ensure_ascii=False, indent=4)


# curr_year = 1970
# genre_structure = []
# countries = [
#     'USA',
#     'United Kingdom',
#     'Germany',
#     'Sweden',
#     'Finland',
# ]
# while curr_year < 2017:
#     date_string = "{}-{}".format(curr_year, curr_year + 5)
#     for country in countries:
#         genre_date_structure = {
#             'country': country,
#             'time': date_string,
#         }
#         for index, row in data_frame.iterrows():
#             if (
#                 row['formed'] == '-' or int(row['formed']) <= (curr_year + 5)
#             ) and (
#                 row['split'] == '-' or int(row['split']) >= (curr_year)
#             ) and (
#                 row['origin'] == country
#             ):
#                 genres = row['style'].split(',')
#                 for genre in genres:
#                     if genre.rstrip() not in genre_date_structure:
#                         genre_date_structure[genre.rstrip()] = 0
#                     genre_date_structure[genre.rstrip()] += row['fans']
#         genre_structure.append(genre_date_structure)
#     curr_year += 5

# # pprint(year_structure)

# import operator


curr_year = 1970
genre_year_structure = {}
while curr_year < 2017:
    date_string = "{}-{}".format(curr_year, curr_year + 5)
    genre_year_structure[date_string] = {}
    for index, row in data_frame.iterrows():
        if (
            row['formed'] == '-' or int(row['formed']) <= (curr_year + 5)
        ) and (
            row['split'] == '-' or int(row['split']) >= (curr_year)
        ):
            genres = row['style'].split(',')
            for genre in genres:
                if genre.rstrip() not in genre_year_structure[date_string]:
                    genre_year_structure[date_string][genre.rstrip()] = 0
                genre_year_structure[date_string][genre.rstrip()] += 1
    curr_year += 5

for (genre_year, genre_obj) in genre_year_structure.items():
    new_obj = {k: v for k, v in sorted(genre_obj.items(), key=lambda item: item[1], reverse=True)}
    print(genre_year)
    for genre in list({k: v for k, v in sorted(genre_obj.items(), key=lambda item: item[1], reverse=True)})[:10]:
      print("{}:\t{}".format(
        genre, genre_obj[genre]
      ))
    print("\n")
    # genre_year[year] = new_obj
    # genre_obj.sort(key=lambda x: x[1], reverse=True)
    # print(year)
    # print("{}:\t{}\n".format(
    #   max(genre_obj.items(), key=operator.itemgetter(1))[0], genre_obj[max(genre_obj.items(), key=operator.itemgetter(1))[0]]
    # ))
# pprint(genre_structure)

import json
with open('genre_data.json', 'w', encoding='utf-8') as f:
    json.dump(genre_structure, f, ensure_ascii=False, indent=4)