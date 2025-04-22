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
                    
                        sh '''
                            python3 -m venv venv
                            . venv/bin/activate
                            sudo pip3 install -r requirements.txt --break-system-packages
                        '''
                    }
                }
            }
        
        stage("Data Ingestion"){
            steps{
                script{
                    
                        sh "python3 data_ingestion.py"
                    }
                }
            
        }
        stage("Data Processing"){
            steps{
                script{
                    
                        sh "python3 data_processing.py"
                    }
                
            }
        }
        stage("Data Validation"){
            steps{
                script{
                    
                        sh "python3 data_validation.py"
                    }
                
            }
        }
        stage("Load to database"){
            steps{
                script{
                    
                        sh "python3 load_to_database.py"
                    }
                
            }
        }
        stage("Report Generation"){
            steps{
                script{
                    
                        sh "python3 generate_report.py"
                        archiveArtifacts artifacts: 'reports/data_insights_report.html', followSymlinks: false
                        archiveArtifacts artifacts: 'reports/correlation_plot.png', followSymlinks: false
                        archiveArtifacts artifacts: 'reports/cluster_plot.png', followSymlinks: false
                    }
                
            }
        }
    }
}
