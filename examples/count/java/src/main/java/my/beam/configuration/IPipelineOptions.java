package apache.beam.configuration;

import org.apache.beam.sdk.options.Default;
import org.apache.beam.sdk.options.Description;
import org.apache.beam.sdk.options.PipelineOptions;

public interface IPipelineOptions extends PipelineOptions{


    @Description("Expansion service URL")
    @Default.String("localhost:8097")
    String getExpansionServiceURL();

    void setExpansionServiceURL(String url);

    @Description("External splitting")
    boolean isUseExternal();

    void setUseExternal(boolean isUseExternal);


}
