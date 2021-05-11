var config = {
    development: {
        //mongodb connection settings
        database: {
            host:   '127.0.0.1',
            port:   '27017',
            DATABASE_NAME: 'DB',
            system_password: 'RANDOM_PASSWORD',
            system_admin: 'ADMIN_USERNAME',
            encryption_secret_key: 'RANDOM_ENCRYPTION_KEY'
        },
        //server details
        server: {
            host: '127.0.0.1',
            port: '3000'
        }
    }
};
module.exports = config;