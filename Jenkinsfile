pipeline {
  agent any

  environment {
    VAULT_ADDR      = credentials('VAULT_ADDR')
    VAULT_ROLE_ID   = credentials('VAULT_ROLE_ID')
    VAULT_SECRET_ID = credentials('VAULT_SECRET_ID')
  }

  stages {

    stage('Vault Login') {
      steps {
        sh '''
          chmod +x ansible/scripts/vault-login.sh
          ./ansible/scripts/vault-login.sh "${VAULT_ADDR}" "${VAULT_ROLE_ID}" "${VAULT_SECRET_ID}"
        '''
      }
    }


    stage('Install Requirements') {
      steps {
        sh '''
          python3 -m venv venv
          source .env
          source venv/bin/activate
          pip install -r requirements.txt
        '''
      }
    }

    stage('Run Ansible Deploy') {
      steps {
        ansiColor('xterm') {
          ansiblePlaybook(
              playbook: './ansible/playbooks/deploy.yml',
              inventory: './ansible/inventories/webs.ini',
              credentialsId: 'ANSIBLE_SSH_KEY',
              colorized: true)
      }}
    }

  }
}

