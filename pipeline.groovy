pipeline{
    agent any
    stages{
        stage("Clone"){
            steps{
                git branch: 'main', url:'https://github.com/AbhishekRaoV/dataops.git'
            }
        }

        stage("Setup Environment"){
            steps{
                script{
                    ws('dataops'){
                        sh '''
                        source venv/bin/activate
                        pip3 install -r requirements.txt
                        '''
                    }
                }
            }
        }
        stage("Data Ingestion"){
            steps{
                script{
                    ws('dataops'){
                        sh "python3 data_ingestion.py"
                    }
                }
            }
        }
        stage("Data Processing"){
            steps{
                script{
                    ws('dataops'){
                        sh "python3 data_processing.py"
                    }
                }
            }
        }
        stage("Data Validation"){
            steps{
                script{
                    ws('dataops'){
                        sh "python3 data_validation.py"
                    }
                }
            }
        }
        stage("Load to database"){
            steps{
                script{
                    ws('dataops'){
                        sh "python3 load_to_database.py"
                    }
                }
            }
        }
        stage("Report Generation"){
            steps{
                script{
                    ws('dataops'){
                        sh "python3 generate_report.py"
                    }
                }
            }
        }
    }
}
