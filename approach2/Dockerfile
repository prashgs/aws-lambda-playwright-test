# Define custom function directory
ARG FUNCTION_DIR="/function"

FROM public.ecr.aws/docker/library/python:buster as build-image

# Include global arg in this stage of the build
ARG FUNCTION_DIR

# Install aws-lambda-cpp build dependencies
RUN apt-get update && \
    apt-get install -y \
    g++ \
    make \
    cmake \
    unzip \
    libcurl4-openssl-dev

# Copy function code
RUN mkdir -p ${FUNCTION_DIR}
COPY . ${FUNCTION_DIR}

# Install the function's dependencies
RUN pip install \
    --target ${FUNCTION_DIR} \
    awslambdaric


FROM public.ecr.aws/docker/library/python:3.11-slim-bookworm

# Include global arg in this stage of the build
ARG FUNCTION_DIR
# Set working directory to function root directory

WORKDIR ${FUNCTION_DIR}

# Copy in the built dependencies
COPY --from=build-image ${FUNCTION_DIR} ${FUNCTION_DIR}

ENV PLAYWRIGHT_BROWSERS_PATH=${FUNCTION_DIR}/ms-playwright

RUN apt-get update

RUN python -m venv venv && \
    . venv/bin/activate

RUN pip install playwright && \
    PLAYWRIGHT_BROWSERS_PATH=${FUNCTION_DIR}/ms-playwright playwright install chromium && \
    playwright install-deps chromium

ENTRYPOINT [ "python", "-m", "awslambdaric" ]
CMD [ "app.handler" ]