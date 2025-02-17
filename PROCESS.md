# Run Application on Docker

## Steps
1. Run the Python application locally outside of Docker. Check the endpoints if accessible and showing correct response
- Findings: No issue with Python application when running locally outside of Docker.
2. Inspect Dockerfile, build image and run container. Check endpoints if accessible and showing correct response
- Findings: 
    - Incorrect port exposed
    - Uses distroless image for production-ready container
    - Container fails to build. Exits immediately.
3. Investigate potential causes
- Check if requirements.txt contains Flask --> It does.
- Check if packages in the build stage are installed and confirm directory location. Used CMD ["tail", "-f", "/dev/null"] to keep container running indefinitely. Confirmed that it installs python 3.8 in /root/.local
- Check issues with final stage. Keep container running using -t command and removing CMD instruction. Use site in python to determine location of sitepackages. Found in /usr/lib/python3.11 -->
    - Match Python version 
    - Change COPY command to correct directory
    - Change port exposed
    - Adjust ENV variables accordingly
    - Adjust CMD instruction, set ENV for FLASK_APP
```
import site

for path in site.getsitepackages():
    print(path)
```
4. Once container does not exit and the flask app is up, check routes if accessible and showing correct response --> It does

# Run Application on Minikube
## Steps
1. Inspect deployment.yaml
- Change ports for liveness and readiness
2. Inspect hpa.yaml
3. Inspect ingress.yaml
4. Inspect service.yaml
- Change target port to 5000
5. Run kubectl apply and fix identified issues
- Remove initContainers section which introduces circular dependency
- Change readinessProbe to use "/healthy" path instead
- Increased CPU Limit to 100m
- Change HPA API version and adjust syntax accordingly
- Change Ingress class name to nginx. Add annotations for regex and URL rewrite. Fix service name typo.
6. Apply the changes and observe if behavior is as intended --> It is, using minikube tunnel and enabling ingress add ons.

# Create Helm Charts 
1. Create templates and values.yaml file
2. Test deploy with helm chart


