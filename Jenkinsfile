@Library('My-Shared-Library') _
pipeline {
  agent any
  parameters {
    choice(name :'action', choices:'create\ndelete', description: 'choose create\ndelete')
    string(name:'ImageName',description:"name of the docker build", defaultValue:'atm-app')
    string(name:'DockerHubUser',description:"name of the Application", defaultValue:'soucherif')
  }
  

  
  
  stages {
    stage('clean workspace'){
      steps{
        script{
          cleanWs()
        }
      }
    }
    
    
    stage('Git checkout') {
      when {
      expression{
        params.action == 'create'
      }
      }
      steps {
        script{
          gitCheckout(
          branch : "main",
          url :"https://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@github.com/soucherif/ATM-Machine.git"
        )
        }
        
      }
    }
    stage('Unit Test Maven') {
      when {
      expression{
        params.action == 'create'
      }
    }
      steps {
        script{
          mvnTest()
        
        }
        
      }
    }
    stage('Integration Test Maven') {
      when {
      expression{
        params.action == 'create'
      }
    }
      steps {
        script{
          mvnIntegrationTest()
        
        }
        
      }
    }
    /*stage('run Selenium test') {
      when {
      expression{
        params.action == 'create'
      }
    }
      steps {
        script{
          seleniumTest()
        }
        
      }
    }*/
    stage('Static Code Analysis : SonarQube') {
      when {
      expression{
        params.action == 'create'
      }
    }
      steps {
        script{
          def SonarQubecredentialsId = 'mytoken'
          statiCodeAnalysis(SonarQubecredentialsId)
        
        }
        
      }
    }
    stage('Quality Gate Status check : SonarQube') {
      when {
      expression{
        params.action == 'create'
      }
    }
      steps {
        script{
          def SonarQubecredentialsId = 'mytoken '
          QualityGateStatus(SonarQubecredentialsId)
        
        }
        
      }
    }
    stage('Maven Build : maven') {
      when {
      expression{
        params.action == 'create'
      }
    }
      steps {
        script{
          mvnBuild()
        
        }
        
      }
    }
    stage('Docker Image Build') {
      when {
      expression{
        params.action == 'create'
      }
    }
      steps {
        script{
          dockerHubBuild("${params.ImageName}","${BUILD_NUMBER}", "${params.DockerHubUser}")
        
        }
        
      }
    }
    stage('Docker Image Scan : Trivy') {
      when {
      expression{
        params.action == 'create'
      }
    }
      steps {
        script{
          dockerHubImageScan("${params.ImageName}","${BUILD_NUMBER}", "${params.DockerHubUser}")
        
        }
        
      }
    }
    stage('Docker Image Push : DockerHub') {
      when {
      expression{
        params.action == 'create'
      }
    }
      steps {
        script{
          dockerHubImagePush("${params.ImageName}","${BUILD_NUMBER}", "${params.DockerHubUser}")
        
        }
        
      }
    }
    stage('Docker Image CleanUp : DockerHub') {
      when {
      expression{
        params.action == 'create'
      }
    }
      steps {
        script{
          dockerHubImageCleanUp("${params.ImageName}","${BUILD_NUMBER}", "${params.DockerHubUser}")
        
        }
        
      }
    }
    stage('Update Kubernetes Deployment File'){
      steps{
        dir('kubernetes'){
          sh " cat deployment.yaml"
          sh "sed -i 's#image:.*#image: ${params.DockerHubUser}/${params.ImageName}:${BUILD_NUMBER}#g' deployment.yaml"
          sh " cat deployment.yaml"

        }
        
      }
    }
    stage('Push the Kubernetes Deployment File'){
      steps{
        dir('kubernetes'){
          sh """
        git config --global user.name "soucherif"
        git config --global user.email "cherifsouhail@outlook.fr"
        git add deployment.yaml
        git commit -m "m"
        """
        /*withCredentials([usernamePassword(credentialsId: 'github', passwordVariable: 'PASS', usernameVariable: 'USER')]) {
           sh "git push  https://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@github.com/soucherif/ATM-Machine.git HEAD:main"    
        }*/

        }
        
        
      }
    }
    
  }
}
              
            
        
  
    


