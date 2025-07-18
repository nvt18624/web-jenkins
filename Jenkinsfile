pipeline {
    agent any
    environment {
        VAULT_ADDR = ''
        VAULT_ROLE_ID = ''
        VAULT_SECRET_ID = ''
    }
    stages {
        stage('Vault Login') {
            steps {
                script {
                    withCredentials([
                        string(credentialsId: 'VAULT_ADDR', variable: 'VAULT_ADDR'),
                        string(credentialsId: 'VAULT_ROLE_ID', variable: 'VAULT_ROLE_ID'),
                        string(credentialsId: 'VAULT_SECRET_ID', variable: 'VAULT_SECRET_ID')
                    ]) {
                        sh '''
                            echo "VAULT_ADDR=$VAULT_ADDR"
                            echo "VAULT_ROLE_ID=$VAULT_ROLE_ID"
                            echo "VAULT_SECRET_ID=$VAULT_SECRET_ID"
                            bash vaul-login.sh
                        '''
                    }
                }
            }
        }
    }
}

