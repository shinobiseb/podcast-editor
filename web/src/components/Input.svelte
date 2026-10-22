<script lang="ts">
  let mediaFiles = $state({
    camera1: null as File | null,
    camera2: null as File | null,
    audio: null as File | null
  });

  let isFilesUploaded = $derived(
    Boolean(mediaFiles.audio && mediaFiles.camera1 && mediaFiles.camera2)
  )

  function handleFileChange(key: keyof typeof mediaFiles, event: Event) {
    const target = event.target as HTMLInputElement;
    mediaFiles[key] = target.files?.[0] ?? null;
  }

  $effect(() => {
      if (isFilesUploaded) {
      console.log("Files uploaded");
      }
  });

  function fillMockFiles() {
    mediaFiles.camera1 = new File(["dummy video content 1"], "cam1_test.mp4", { type: "video/mp4" });
    mediaFiles.camera2 = new File(["dummy video content 2"], "cam2_test.mp4", { type: "video/mp4" });
    mediaFiles.audio = new File(["dummy audio content"], "audio_test.wav", { type: "audio/wav" });
  }
</script>

<main>
  <button style="margin-bottom: 1rem; background: #e0e0e0; cursor: pointer;" onclick={fillMockFiles}>
      ⚡ Auto-Fill Mock Files (Dev)
  </button>

  <div>
    <label for="cam1">Camera 1:</label>
    <input type="file" id="cam1" onchange={(e) => handleFileChange('camera1', e)}>
  </div>

  <div>
    <label for="cam2">Camera 2:</label>
    <input type="file" id="cam2" onchange={(e) => handleFileChange('camera2', e)}>
  </div>

  <div>
    <label for="aud">Audio:</label>
    <input type="file" id="aud" onchange={(e) => handleFileChange('audio', e)}>
  </div>

  <hr>

  <h3>Selected Files:</h3>
  <p>Camera 1: <strong>{mediaFiles.camera1?.name ?? 'None'}</strong></p>
  <p>Camera 2: <strong>{mediaFiles.camera2?.name ?? 'None'}</strong></p>
  <p>Audio: <strong>{mediaFiles.audio?.name ?? 'None'}</strong></p>
  {#if isFilesUploaded}
    <p>Files Uploaded Successfully! Press Submit to Upload for Processing</p>
    <button>Submit</button>
  {/if}
</main>