# from django.db import connection
# import time


# class SQLLoggingMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         start_time = time.time()

#         response = self.get_response(request)

#         elapsed_time = time.time() - start_time

#         for query in connection.queries:
#             print(f"SQL Query: {query['sql']}")
#             print(f"Execution time: {query['time']}s")

#         print(f"Total time for request: {elapsed_time:.3f}s")
#         return response
