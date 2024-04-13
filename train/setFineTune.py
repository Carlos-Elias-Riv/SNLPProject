import replicate

training = replicate.trainings.create(
    version="meta/llama-2-7b:73001d654114dad81ec65da3b834e2f691af1e1526453189b7bf36fb3f32d0f9",
    input={
    "train_data": "https://replicate.delivery/pbxt/KhSfUm87PVH4VPxN6vRLbxcML5zydAMTlvAYdHVDdLPQtJWx/data.jsonl",
    "num_train_epochs": 3
    },
    destination="carlos-elias-riv/llama2-semanticsimilarity"
)

print(training)
