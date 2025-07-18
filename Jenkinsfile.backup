pipeline {
  agent any

  environment {
    VAULT_ADDR      = credentials('VAULT_ADDR')
    VAULT_ROLE_ID   = credentials('VAULT_ROLE_ID')
    VAULT_SECRET_ID = credentials('VAULT_SECRET_ID')
    ANSIBLE_SSH_KEY = credentials('ANSIBLE_SSH_KEY')
  }

  stages {
    stage('Checkout') {
      steps {
        git credentialsId: 'jenkins-thiennguyen', url: 'https://github.com/nvt18624/web-jenkins.git', branch: 'main'
      }
    }

    stage('Install Requirements') {
      steps {
        sh '''
          python3 -m venv venv
          source venv/bin/activate
          pip install -r requirements.txt
        '''
      }
    }

    stage('Vault Login') {
      steps {
        sh '''
          chmod +x ansible/scripts/vault-login.sh
          ./ansible/scripts/vault-login.sh "${VAULT_ADDR}" "${VAULT_ROLE_ID}" "${VAULT_SECRET_ID}"
        '''
      }
    }

    stage('Run Ansible Deploy') {
      steps {
        sh '''
          ansible-playbook -i ansible/inventory/hosts.ini ansible/playbook.yml \
            --private-key=${ANSIBLE_SSH_KEY} \
            --extra-vars "vault_addr=${VAULT_ADDR} vault_role_id=${VAULT_ROLE_ID} vault_secret_id=${VAULT_SECRET_ID}"
        '''
      }
    }
  }
}

