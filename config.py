
# Ports for your workers
STRATUM_HOST = "0.0.0.0"
STRATUM_PORT = 8080

# Coin address where money goes. If you mine direct to the exchange, you MUST specify payment_id together with wallet of exchange.
WALLET = '4A6xNd9dSaqL29V2mzpzDFfcUg4JG4wy2PZq5iAmy9ezXvvsVaYzdCPhikXYYTQ54DWpT7VVSfen6LqfgoNPmuP5Cz8o5ZR'
# Only if you mine direct to the exchange
PAYMENT_ID = ''

# It's useful for individually monitoring and statistic.
# In your workers you have to use any number as username (without wallet!)
ENABLE_WORKER_ID = True
WORKER_ID_FROM_IP = False

# On DwarfPool you have option to monitor your workers via email.
# If WORKER_ID is enabled, you can monitor every worker/rig separately.
MONITORING = True
MONITORING_EMAIL = 'mail@example.com'

# Main pool
POOL_HOST = 'xmr-eu.dwarfpool.com'
POOL_PORT = 8050

# Failover pool
POOL_FAILOVER_ENABLE = False
POOL_HOST_FAILOVER = 'xmr-usa.dwarfpool.com'
POOL_PORT_FAILOVER = 8050

# ERROR, INFO, DEBUG
LOGLEVEL = 'DEBUG'
DEBUG = False
LOGFILE = "logfile.log"
