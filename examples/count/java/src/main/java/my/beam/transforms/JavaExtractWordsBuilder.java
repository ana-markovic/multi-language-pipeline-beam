package my.beam.transforms;

import org.apache.beam.sdk.transforms.PTransform;
import org.apache.beam.sdk.values.PCollection;
import org.apache.beam.sdk.transforms.ExternalTransformBuilder;

public class JavaExtractWordsBuilder implements
    ExternalTransformBuilder<JavaExtractWordsConfiguration, PCollection<String>, PCollection<String>> {

  @Override
  public PTransform<PCollection<String>, PCollection<String>> buildExternal(
      JavaExtractWordsConfiguration configuration) {
    return new JavaExtractWords();
  }
}
