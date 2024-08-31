import json
# from collections import defaultdict
#
# with open('weather_data.json', 'r') as file:
#     weather_data = json.load(file)
#
# city_temps = defaultdict(lambda: [0, 0])
#
# for city_info in weather_data['weather']:
#     city = city_info['city']
#     temp = city_info['temperature']
#     city_temps[city][0] += temp
#     city_temps[city][1] += 1
#
# city_avg_temps = {city: round(sum_temp / count_days, 2) for city, (sum_temp, count_days) in city_temps.items()}
# highest_avg_city = max(city_avg_temps, key=city_avg_temps.get)
# highest_avg_temp = city_avg_temps[highest_avg_city]
#
# print(f"Город с самой высокой средней температурой: {highest_avg_city}, Средняя температура: {highest_avg_temp}")

# ********************************

# with open('movies.json', 'r') as file:
#     movie_data = json.load(file)
# filtered_movies = []
#
# for movie in movie_data['movies']:
#     if movie['year'] > 2015 and movie['rating'] > 7:
#         filtered_movies.append(movie)
#
# with open('filtered_movies.json', 'w') as file:
#     json.dump({'movies': filtered_movies}, file, indent=4)
#
# print("Фильтрование завершено, результаты сохранены в filtered_movies.json")

# *********************************
# from collections import defaultdict
# with open('sales.json', 'r') as file:
#     sales_data = json.load(file)
#
# product_sales = defaultdict(lambda: [0, 0])
#
# for sale in sales_data['sales']:
#     product = sale['product']
#     total_sale = sale['total']
#     quantity_sold = sale['quantity']
#     product_sales[product][0] += total_sale
#     product_sales[product][1] += quantity_sold
#
# total_store_revenue = sum(sales[0] for sales in product_sales.values())
#
# sales_report = {
#     'total_store_revenue': total_store_revenue,
#     'product_sales': {
#         product: {
#             'total_sales': sales[0],
#             'quantity_sold': sales[1]
#         }
#         for product, sales in product_sales.items()
#     }
# }
#
# with open('sales_report.json', 'w') as file:
#     json.dump(sales_report, file, indent=4)
#
# print("Отчет по продажам создан и сохранен в sales_report.json")




