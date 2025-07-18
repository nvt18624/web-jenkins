pipeline {
  agent any

  environment {
    VAULT_ADDR      = credentials('VAULT_ADDR')       // string credential
    VAULT_ROLE_ID   = credentials('VAULT_ROLE_ID')    // string credential
    VAULT_SECRET_ID = credentials('VAULT_SECRET_ID')  // string credential
  }

  stages {

    stage('Vault Login & Generate .env') {
      steps {
        sh '''
          echo "[INFO] Logging into Vault and generating .env file..."
          chmod +x ./scripts/vault_login.sh
          ./scripts/vault_login.sh "${VAULT_ADDR}" "${VAULT_ROLE_ID}" "${VAULT_SECRET_ID}"
        '''
      }
    }

    stage('Ansible Deploy') {
      steps {
        ansiColor('xterm') {
          ansiblePlaybook(
            playbook: './ansible/playbooks/deploy.yml',
            inventory: './ansible/inventories/webs.ini',
            credentialsId: 'ANSIBLE_SSH_KEY',
            colorized: true
          )
        }
      }
    }
  }
}

