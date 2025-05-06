pipeline {
    agent {
        docker {
            image 'python:3.10'
        }
    }
    
    stages {
        stage('Install Curl') {
            steps {
                sh 'apt-get update && apt-get install -y curl'
            }
        }
        stage('Install Depencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Test') {
            steps {
                sh 'pytest test_app.py'
            }
        }
        stage('Deploy') {
            when {
                anyOf {
                    branch 'main'
                    branch pattern: "release/.*", comprator: "REGEXP"
                }
            }
            steps {
                echo "Simulating deploy from branch ${env.BRANCH_NAME}"
            }
        }
    }

post {
    success {
        sh """
        curl -H "Content-Type: application/json" \
             -X POST \
             -d '{"content":"✅ Build SUCCESS on branch ${env.BRANCH_NAME}"}' \
             https://discord.com/api/webhooks/1369197474174074961/d92R5Wvj2_7NOsFNajK-GOmTdZMRDwIlYpNmBHiKZq2YHoD3HUipDuo4uo19nddjGFJZ'
        """
    }
    failure {
        sh """
        curl -H "Content-Type: application/json" \
             -X POST \
             -d '{"content":"❌ Build FAILED on branch ${env.BRANCH_NAME}"}' \
             https://discord.com/api/webhooks/1369197474174074961/d92R5Wvj2_7NOsFNajK-GOmTdZMRDwIlYpNmBHiKZq2YHoD3HUipDuo4uo19nddjGFJZ'
        """
    }
}

}
