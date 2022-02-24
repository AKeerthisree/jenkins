pipeline {
agent any
 stages {
  stage('Clone Git') {
   steps {
    git 'https://github.com/AKeerthisree/jenkins.git'
   }
  }
  stage('Build Code') {
   steps {
    sh "chmod u+x prog1.py"
    sh "python3 ./prog1.py"
   }
  }
  stage('Test Code') {
   steps {
    sh "chmod u+x test.py"
    sh "python3 ./test.py"
   }
  }
 }
}
