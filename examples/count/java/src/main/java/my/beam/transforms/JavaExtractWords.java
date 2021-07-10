package my.beam.transforms;

import org.apache.beam.sdk.Pipeline;
import org.apache.beam.sdk.transforms.*;
import org.apache.beam.sdk.values.PCollection;
import org.apache.beam.sdk.values.TypeDescriptors;

import java.util.Arrays;
import java.util.Map;

public class JavaExtractWords extends PTransform<PCollection<String>, PCollection<String>> {

  public JavaExtractWords() {
  }

 @Override
 public PCollection<String> expand (PCollection<String> input){

   return input.apply("ExtractWords", FlatMapElements
           .into(TypeDescriptors.strings())
           .via((String line) -> Arrays.asList(line.split("[^\\p{L}]+"))));

  }
}
