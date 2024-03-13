import hashlib

def generate_api_sig(rand, method_name, params, secret):
    # Формируем строку запроса
    sorted_params = '&'.join([f'{param}={params[param]}' for param in sorted(params.keys())])
    query_string = f'{rand}/{method_name}?{sorted_params}#{secret}'

    # Вычисляем SHA-512 хеш
    hash_code = hashlib.sha512(query_string.encode()).hexdigest()

    return hash_code