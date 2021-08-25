package my.beam.transforms;

import org.apache.beam.sdk.transforms.PTransform;
import org.apache.beam.sdk.values.KV;
import org.apache.beam.sdk.values.PCollection;
import org.apache.beam.sdk.transforms.ExternalTransformBuilder;

public class JavaExtractWordsBuilder implements
        ExternalTransformBuilder<JavaExtractWordsConfiguration, PCollection<String>, PCollection<KV<String, Long>>> {

  @Override
  public PTransform<PCollection<String>, PCollection<KV<String, Long>>> buildExternal(
          JavaExtractWordsConfiguration configuration) {
    return new JavaExtractWords(configuration.prefix);
  }
}
