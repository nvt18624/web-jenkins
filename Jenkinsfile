pipeline {
  agent any

  environment {
    VAULT_ADDR      = credentials('VAULT_ADDR')
    VAULT_ROLE_ID   = credentials('VAULT_ROLE_ID')
    VAULT_SECRET_ID = credentials('VAULT_SECRET_ID')
  }

  stages {
    stage('Vault Login & Generate .env') {
      steps {
        sh '''
          echo "[INFO] Logging into Vault and generating .env file..."
          chmod +x ./scripts/vault_login.sh
          ./scripts/vault_login.sh "${VAULT_ADDR}" "${VAULT_ROLE_ID}" "${VAULT_SECRET_ID}"
          ls -al ./
          ls -al ./app/
        '''
        stash includes: 'app/.env', name: 'env-file'
      }
    }

    stage('Ansible Deploy') {
      steps {
        unstash 'env-file'

        withCredentials([
          sshUserPrivateKey(credentialsId: 'GG_CLOUD_PRIVATE', keyFileVariable: 'KEY_FILE')
        ]) {
          sh '''
            echo "[INFO] Using SSH key at $KEY_FILE"

            mkdir -p ~/.ssh
            chmod 700 ~/.ssh

            echo "[INFO] Writing SSH config..."
            cat << EOF > ~/.ssh/config
        Host bastion
          HostName 34.66.23.89
          User tn18624
          IdentityFile $KEY_FILE
          StrictHostKeyChecking no
          UserKnownHostsFile=/dev/null

        Host 10.0.2.*
          User tn18624
          IdentityFile $KEY_FILE
          ProxyJump bastion
          StrictHostKeyChecking no
          UserKnownHostsFile=/dev/null
        EOF

            chmod 600 ~/.ssh/config
            chmod 600 "$KEY_FILE"

            echo "[INFO] Running Ansible playbook..."
            cd ansible
            ansible-playbook ./playbooks/deploy.yml -i ./inventories/webs.ini -vvvv
          '''
        }

      }
    }
  }
}
