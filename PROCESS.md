# Steps
1. Run the Python application locally. Check the endpoints if accessible and showing correct response
- Findings: No issue with Python application when running locally.
2. Inspect Dockerfile, build image and run container. Check endpoints if accessible and showing correct response
- Findings: 
    - Incorrect port exposed
    - Uses distroless image for production-ready container
    - Container fails to build. Exits immediately.
3. Investigate potential causes
- Check if requirements.txt contains Flask --> It does.
- Check if packages in the build stage are installed and confirm directory location. Used CMD ["tail", "-f", "/dev/null"] to keep container running indefinitely. Confirmed that it installs python 3.8 in .root/local


