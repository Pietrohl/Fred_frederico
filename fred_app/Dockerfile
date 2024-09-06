FROM python:3 as build

RUN mkdir -p /home/app

COPY ./fred_app ./requirements.txt /home/app/

WORKDIR /home/app

RUN pip install --no-cache-dir .

FROM gcr.io/distroless/python3

COPY --from=build /home/app /home/app/


CMD ["flask", "--app", "fred_app", "run"]