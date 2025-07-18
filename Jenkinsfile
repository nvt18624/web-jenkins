pipeline {
    agent any

    stages {
        stage('Clone code') {
            steps {
                git 'https://github.com/nvt18624/web-jenkins.git'
            }
        }

        stage('Get Vault Secrets') {
            steps {
                withCredentials([
                    string(credentialsId: 'VAULT_ROLE_ID', variable: 'VAULT_ROLE_ID'),
                    string(credentialsId: 'VAULT_SECRET_ID', variable: 'VAULT_SECRET_ID'),
                    string(credentialsId: 'VAULT_ADDR', variable: 'VAULT_ADDR')
                ]) {
                    sh 'bash scripts/vault_login.sh'
                }
            }
        }

        stage('Deploy with Ansible') {
            steps {
                ansiblePlaybook(
                    credentialsId: 'ANSIBLE_SSH_KEY',     
                    inventory: 'ansible/inventories/webs.ini',          
                    playbook: 'ansible/playbooks/deploy.yml',
                    extras: '--extra-vars "@.env"'
                )
            }
        }
    }
}

