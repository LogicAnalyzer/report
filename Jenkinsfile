pipeline{
	agent any
	stages{
		stage("Build"){
			steps{
				[ -e report.pdf ] && rm report.pdf
				python3 generate.py
			}
		}
	}
}