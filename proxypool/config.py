from random import choice

# output to stdout
VERBOSE = True

# server
HOST = '0.0.0.0'
PORT = 8088
SERVER_ON = False

SSL_ON = False
CERT = '/path/to/your/server.crt'
KEY = '/path/to/your/server.key'
PASSWORD = None
CA_CRT = '/path/to/your/ca.crt'
if SSL_ON:
    SCHEME = 'https'
else:
    SCHEME = 'http'

# redis
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379

# pool
UPPER_LIMIT = 2000
LOWER_LIMIT = 500
# when size of pool equal upper_limit*upper_limit_ratio, stopped crawl pages, but validator continued,
# so the size of pool was still increasing
UPPER_LIMIT_RATIO = 0.85

# check and validate
CHECK_CYCLE_TIME = 900     # the cycle of check proxies count
CHECK_INTERVAL_TIME = 1200  # the time between crawler finished and next check
VALIDATE_CYCLE_TIME = 600 # the cycle of validate proxies in pool
VALIDATE_UPPER_LIMIT = 200
VALIDATE_RATIO = 0.25      # validated proxies ratio in pool each time
VALIDATE_TIMEOUT = 3

# coroutines
CORO_COUNT = 50

# crawler
PHANTOMJS_PATH = '/home/shrike/software/phantomjs/bin/phantomjs'
DELAY = 5 # delay between download each web page
USER_AGENT = [
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_0_3; en-US) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.3177.341 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.3350.140 Safari/537.36',
    'Mozilla/5.0 (Windows XP; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.1125.217 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.1661.376 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2613.269 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.3137.300 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.3890.121 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.1027.137 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.1205.300 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.3581.112 Safari/537.36',
    'Mozilla/5.0 (Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2810.129 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.1048.151 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.1954.133 Safari/537.36',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_0_3; en-US) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.1681.179 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.3887.239 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.1727.119 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.1858.371 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.3438.198 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.1119.153 Safari/537.36',
    'Mozilla/5.0 (Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.3062.340 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.3920.111 Safari/537.36',
    'Mozilla/5.0 (Windows XP; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2850.170 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.3509.170 Safari/537.36',
    'Mozilla/5.0 (Windows XP; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2052.214 Safari/537.36',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_0_3; en-US) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2137.255 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2919.396 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2054.290 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.1699.341 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2511.201 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.3644.274 Safari/537.36',
    'Mozilla/5.0 (Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2756.213 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2002.121 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2040.251 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2025.105 Safari/537.36',
    'Mozilla/5.0 (Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2614.239 Safari/537.36',
    'Mozilla/5.0 (Windows XP) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2962.154 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.3727.103 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.1062.191 Safari/537.36',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_0_3; en-US) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.1628.369 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.1577.140 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.1568.360 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.3757.229 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2798.301 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.3850.381 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.1567.118 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.1106.220 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.3125.337 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.3778.273 Safari/537.36',
    'Mozilla/5.0 (Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.3722.281 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2113.164 Safari/537.36',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_0_3; en-US) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2608.175 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.1362.118 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2033.246 Safari/537.36',
    'Mozilla/5.0 (Windows XP; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.3776.362 Safari/537.36',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_0_3; en-US) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.1247.117 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2603.217 Safari/537.36',
    'Mozilla/5.0 (Windows XP; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2500.315 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.3095.212 Safari/537.36',
    'Mozilla/5.0 (Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2042.162 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.1500.269 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2124.186 Safari/537.36',
    'Mozilla/5.0 (Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.3070.316 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.1994.311 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.1053.275 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.3904.160 Safari/537.36',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_0_3; en-US) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.3701.372 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.1102.262 Safari/537.36',
    'Mozilla/5.0 (Windows XP; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.1262.233 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.1839.238 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.1989.382 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2366.316 Safari/537.36',
    'Mozilla/5.0 (Windows XP; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2128.144 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.1932.119 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.3933.345 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2787.173 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.3651.309 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.1180.103 Safari/537.36',
    'Mozilla/5.0 (Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.3533.261 Safari/537.36',
    'Mozilla/5.0 (Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2363.134 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2829.126 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2585.190 Safari/537.36',
    'Mozilla/5.0 (Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.3789.130 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.1096.198 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2663.197 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.3146.381 Safari/537.36',
    'Mozilla/5.0 (Windows XP) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.1701.252 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.1985.365 Safari/537.36',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_0_3; en-US) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.3154.221 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2864.375 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.3271.328 Safari/537.36',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_0_3; en-US) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2031.335 Safari/537.36',
    'Mozilla/5.0 (Windows XP; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.1301.198 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.1737.170 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2496.357 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.1232.107 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.3104.128 Safari/537.36',
    'Mozilla/5.0 (Windows XP; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2767.371 Safari/537.36',
    'Mozilla/5.0 (Windows XP) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2377.338 Safari/537.36',
    'Mozilla/5.0 (Windows XP) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2590.284 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2564.311 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; WOW64) Gecko/20100101 Firefox/47.6',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_0_3; en-US) Gecko/20100101 Firefox/46.0',
    'Mozilla/5.0 (Windows NT 10.0) Gecko/20100101 Firefox/47.7',
    'Mozilla/5.0 (Linux i686) Gecko/20100101 Firefox/48.5',
    'Mozilla/5.0 (Windows NT 5.1; WOW64) Gecko/20100101 Firefox/47.5',
    'Mozilla/5.0 (Windows XP) Gecko/20100101 Firefox/49.9',
    'Mozilla/5.0 (Windows NT 6.1) Gecko/20100101 Firefox/46.1',
    'Mozilla/5.0 (Linux i686) Gecko/20100101 Firefox/45.2',
    'Mozilla/5.0 (Windows NT 6.0) Gecko/20100101 Firefox/46.5',
    'Mozilla/5.0 (Linux i686) Gecko/20100101 Firefox/46.0',
    'Mozilla/5.0 (Linux i686) Gecko/20100101 Firefox/47.6',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) Gecko/20100101 Firefox/49.9',
    'Mozilla/5.0 (Windows NT 6.0; WOW64) Gecko/20100101 Firefox/48.6',
    'Mozilla/5.0 (Windows NT 10.0) Gecko/20100101 Firefox/48.4',
    'Mozilla/5.0 (Windows XP; WOW64) Gecko/20100101 Firefox/47.9',
    'Mozilla/5.0 (Linux x86_64) Gecko/20100101 Firefox/46.5',
    'Mozilla/5.0 (Windows NT 6.1) Gecko/20100101 Firefox/48.1',
    'Mozilla/5.0 (Windows NT 5.1) Gecko/20100101 Firefox/49.7',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) Gecko/20100101 Firefox/49.2',
    'Mozilla/5.0 (Windows XP; WOW64) Gecko/20100101 Firefox/47.4',
    'Mozilla/5.0 (Windows NT 5.1; WOW64) Gecko/20100101 Firefox/47.9',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) Gecko/20100101 Firefox/45.9',
    'Mozilla/5.0 (Windows NT 5.1; WOW64) Gecko/20100101 Firefox/46.1',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_0_3; en-US) Gecko/20100101 Firefox/47.1',
    'Mozilla/5.0 (Windows NT 10.0) Gecko/20100101 Firefox/47.5',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/48.4',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_0_3; en-US) Gecko/20100101 Firefox/47.7',
    'Mozilla/5.0 (Linux x86_64) Gecko/20100101 Firefox/48.1',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/45.8',
    'Mozilla/5.0 (Windows XP) Gecko/20100101 Firefox/45.4',
    'Mozilla/5.0 (Windows NT 6.0; WOW64) Gecko/20100101 Firefox/46.8',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) Gecko/20100101 Firefox/45.0',
    'Mozilla/5.0 (Windows NT 6.1) Gecko/20100101 Firefox/46.1',
    'Mozilla/5.0 (Windows XP) Gecko/20100101 Firefox/48.3',
    'Mozilla/5.0 (Windows NT 6.0) Gecko/20100101 Firefox/49.4',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_0_3; en-US) Gecko/20100101 Firefox/49.3',
    'Mozilla/5.0 (Windows NT 6.1) Gecko/20100101 Firefox/47.3',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) Gecko/20100101 Firefox/45.2',
    'Mozilla/5.0 (Windows XP; WOW64) Gecko/20100101 Firefox/48.3',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/45.6',
    'Mozilla/5.0 (Linux i686) Gecko/20100101 Firefox/45.0',
    'Mozilla/5.0 (Windows NT 10.0) Gecko/20100101 Firefox/47.7',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) Gecko/20100101 Firefox/49.6',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_0_3; en-US) Gecko/20100101 Firefox/45.3',
    'Mozilla/5.0 (Windows NT 6.0; WOW64) Gecko/20100101 Firefox/46.9',
    'Mozilla/5.0 (Windows XP; WOW64) Gecko/20100101 Firefox/45.7',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) Gecko/20100101 Firefox/46.9',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) Gecko/20100101 Firefox/48.1',
    'Mozilla/5.0 (Windows XP) Gecko/20100101 Firefox/45.5',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) Gecko/20100101 Firefox/49.7',
    'Mozilla/5.0 (Windows NT 5.1; WOW64) Gecko/20100101 Firefox/47.4',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) Gecko/20100101 Firefox/47.3',
    'Mozilla/5.0 (Linux i686) Gecko/20100101 Firefox/46.7',
    'Mozilla/5.0 (Windows XP; WOW64) Gecko/20100101 Firefox/48.9',
    'Mozilla/5.0 (Linux x86_64) Gecko/20100101 Firefox/49.7',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) Gecko/20100101 Firefox/47.8',
    'Mozilla/5.0 (Windows NT 10.0) Gecko/20100101 Firefox/49.9',
    'Mozilla/5.0 (Linux x86_64) Gecko/20100101 Firefox/46.8',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) Gecko/20100101 Firefox/45.1',
    'Mozilla/5.0 (Windows NT 6.1) Gecko/20100101 Firefox/48.7',
    'Mozilla/5.0 (Windows XP; WOW64) Gecko/20100101 Firefox/45.0',
    'Mozilla/5.0 (Linux i686) Gecko/20100101 Firefox/49.3',
    'Mozilla/5.0 (Windows NT 5.1) Gecko/20100101 Firefox/47.2',
    'Mozilla/5.0 (Windows NT 6.0; WOW64) Gecko/20100101 Firefox/47.8',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) Gecko/20100101 Firefox/47.4',
    'Mozilla/5.0 (Linux i686) Gecko/20100101 Firefox/45.0',
    'Mozilla/5.0 (Linux i686) Gecko/20100101 Firefox/48.0',
    'Mozilla/5.0 (Windows NT 6.1) Gecko/20100101 Firefox/49.5',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) Gecko/20100101 Firefox/45.0',
    'Mozilla/5.0 (Windows NT 6.1) Gecko/20100101 Firefox/45.0',
    'Mozilla/5.0 (Linux i686) Gecko/20100101 Firefox/46.4',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) Gecko/20100101 Firefox/49.5',
    'Mozilla/5.0 (Windows XP; WOW64) Gecko/20100101 Firefox/45.3',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_0_3; en-US) Gecko/20100101 Firefox/47.7',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) Gecko/20100101 Firefox/49.4',
    'Mozilla/5.0 (Windows XP; WOW64) Gecko/20100101 Firefox/49.1',
    'Mozilla/5.0 (Windows NT 6.0) Gecko/20100101 Firefox/45.1',
    'Mozilla/5.0 (Windows XP) Gecko/20100101 Firefox/46.2',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) Gecko/20100101 Firefox/48.7',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) Gecko/20100101 Firefox/45.1',
    'Mozilla/5.0 (Linux x86_64) Gecko/20100101 Firefox/45.8',
    'Mozilla/5.0 (Windows NT 6.0) Gecko/20100101 Firefox/47.1',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) Gecko/20100101 Firefox/47.4',
    'Mozilla/5.0 (Windows NT 5.1; WOW64) Gecko/20100101 Firefox/47.7',
    'Mozilla/5.0 (Windows NT 6.2) Gecko/20100101 Firefox/47.3',
    'Mozilla/5.0 (Windows XP; WOW64) Gecko/20100101 Firefox/45.3',
    'Mozilla/5.0 (Windows NT 6.1) Gecko/20100101 Firefox/49.3',
    'Mozilla/5.0 (Windows NT 6.1) Gecko/20100101 Firefox/46.8',
    'Mozilla/5.0 (Windows NT 6.2) Gecko/20100101 Firefox/47.1',
    'Mozilla/5.0 (Windows XP; WOW64) Gecko/20100101 Firefox/48.5',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_0_3; en-US) Gecko/20100101 Firefox/45.4',
    'Mozilla/5.0 (Windows NT 6.0; WOW64) Gecko/20100101 Firefox/48.6',
    'Mozilla/5.0 (Windows NT 6.2) Gecko/20100101 Firefox/48.1',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) Gecko/20100101 Firefox/47.5',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) Gecko/20100101 Firefox/49.4',
    'Mozilla/5.0 (Windows NT 10.0) Gecko/20100101 Firefox/48.9',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/49.6',
    'Mozilla/5.0 (Linux i686) Gecko/20100101 Firefox/46.1',
    'Mozilla/5.0 (Windows NT 6.0) Gecko/20100101 Firefox/49.5',
    'Mozilla/5.0 (Windows XP; WOW64) Gecko/20100101 Firefox/48.0'
]

HEADERS = {
    'User-Agent': choice(USER_AGENT),
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8'
}