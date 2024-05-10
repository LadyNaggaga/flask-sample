# Aspire Dashboard ♥️ Flask
To run the Aspire Dashboard first run:

```cli
docker run --rm -it -p 18888:18888 -p 4317:18889 -d --name aspire-dashboard \
    mcr.microsoft.com/dotnet/nightly/aspire-dashboard:8.0.0-preview.6
```

To run this application:

```cli
flask --debug run
```
