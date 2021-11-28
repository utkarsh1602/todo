pipeline{
  agent any
  stages{
    stage("build"){
      steps{
        echo "Building the project"
        sh "python app.py" 
      }
    }
    
    stage("Test"){
      steps{
        echo "Test the project"
      }
    }
  }
}
